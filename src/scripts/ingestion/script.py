import pandas as pd
import re
import psycopg2
import datetime
from datetime import date
import numpy as np


DATABASE_HOST = env('DATABASE_HOST')
now = datetime.datetime.now()


try: 
    connection = psycopg2.connect(
        host=DATABASE_HOST,
        user="root",
        password="root",
        database="Creditoo"
    )
    cursor = connection.cursor()
    print('Conexión establecida ')


    #Basedatos.csv
    database = pd.read_csv('/Users/cohen/Desktop/work/credito-old-api/creditoo-api/src/scripts/ingestion/Database.csv', parse_dates={'Ultimo pago': ['Fecha ultimo pago']}, infer_datetime_format=True)
    dataframe = pd.DataFrame()
    dataframe['Nombre deudor'] = database['Nombre del Cliente']
    dataframe['Celular'] = database['Celular']
    dataframe['Codigo referencia'] = database['Llave']
    dataframe['Cedula'] = database['Cedula ']
    dataframe['Direccion del cliente'] = database['Nombre Ciudad'] + ' ' +  database['Direccion del Cliente']
    dataframe['Tramo'] = database['Tramo inicial']
    dataframe['Dias en mora'] = database['DIAS DE NO PAGO']
    dataframe['Saldo en mora'] = database['SALDO Total adeudado']
    dataframe['Total a pagar'] = database['Total a pagar']
    dataframe['Ultimo pago'] = database['Ultimo pago'].replace({np.nan: '01/01/1997'})
    dataframe['Estado'] = database['Estado inicial']

    
    #Emails.csv
    emails = pd.read_csv('/Users/cohen/Desktop/work/credito-old-api/creditoo-api/src/scripts/ingestion/Emails.csv')
    emails_dataframe = pd.DataFrame()
    emails_dataframe['Cedula'] = emails['Codigo del Cliente']
    emails_dataframe['Email'] = emails['Email'].replace({"NOTIENE@CORREO.COM" : None, "NOTIENE@GMAIL.COM": None })

    #Merge Database.csv with Emails.csv
    dataframe_merge = pd.merge(dataframe, emails_dataframe[['Cedula', 'Email']])

    #SOLO TRAIGO 5 ROWS para poder trabajar comodo
    for indice_fila, fila in dataframe_merge.head(5).iterrows():
        numeros = re.split("CE:|-|Ext:0", fila['Celular'])
        numeros = list(filter(str.strip, numeros))
        numeros_concat = ''
        
        cursor.execute("""SELECT id FROM cartera_persona""")
        id_persona = cursor.fetchall()

        cursor.execute(""" SELECT id  FROM cartera_obligacionfinanciera """)
        id_obligacion = cursor.fetchall()

        query_cuentas= """
            INSERT INTO cartera_cuentasporcobrar(
                periodo, 
                estado_obligacion, 
                fecha_ultimo_pago, 
                tramo, 
                dias_mora, 
                saldo_vencido, 
                total_pagar, 
                obligacion_id, 
                creado, 
                actualizado
                ) VALUES ('%s', '%s','%s', '%s','%s', '%s','%s', '%s','%s', '%s')
        """% ('INICIAL', 
        fila['Estado'], 
        fila['Ultimo pago'], 
        fila['Tramo'], 
        fila['Dias en mora'], 
        1000000, 
        3000000, 
        id_obligacion[indice_fila][0], 
        now.strftime("%Y/%m/%d %H:%M:%S"), 
        now.strftime("%Y/%m/%d %H:%M:%S"))

        cursor.execute(query_cuentas)
        print('Success 🟢')
        connection.commit()
        
        
        query_obligacion = """
             INSERT INTO cartera_obligacionfinanciera (numero_referencia, cliente_id, persona_id) VALUES ('%s', '%s', '%s')
        """%(fila['Codigo referencia'], 1, id_persona[indice_fila][0])

        

        for numero in numeros:
            numeros_concat += '' + numero
            query_persona = """
                INSERT INTO cartera_persona (numero_identificacion, tipo_identification, telefono, direccion, nombre, email, creado, actualizado) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
            """ % (int(fila['Cedula']), 'CC', numeros_concat, fila['Direccion del cliente'], fila['Nombre deudor'], fila['Email'], now.strftime("%Y/%m/%d %H:%M:%S"), now.strftime("%Y/%m/%d %H:%M:%S"))
        
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print('Conexión cerrada ')
