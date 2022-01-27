import pandas as pd
import re
import psycopg2
import datetime
import numpy as np



now = datetime.datetime.now()


try: 
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="cohen",
        database="Pruebas"
    )
    cursor = connection.cursor()
    print('Conexión establecida ')


    #Basedatos.csv
    database = pd.read_csv('/Users/cohen/Desktop/work/credito-old-api/creditoo-api/src/scripts/ingestion/Database.csv')
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
    dataframe['Fecha ultimo pago'] = database['Fecha ultimo pago'].replace({np.nan: None})
    dataframe['Estado'] = database['Estado inicial']

    
    #Emails.csv
    emails = pd.read_csv('/Users/cohen/Desktop/work/credito-old-api/creditoo-api/src/scripts/ingestion/Emails.csv')
    emails_dataframe = pd.DataFrame()
    emails_dataframe['Cedula'] = emails['Codigo del Cliente']
    emails_dataframe['Email'] = emails['Email'].replace({"NOTIENE@CORREO.COM" : None, "NOTIENE@GMAIL.COM": None })

    #Merge Database.csv with Emails.csv
    dataframe_merge = pd.merge(dataframe, emails_dataframe[['Cedula', 'Email']])


    for indice_fila, fila in dataframe_merge.head(5).iterrows():
        numeros = re.split("CE:|-|Ext:0", fila['Celular'])
        numeros = list(filter(str.strip, numeros))
        numeros_concat = ''
        id_concat = ''
        cursor.execute("""SELECT id FROM cartera_persona""")
        id_ = cursor.fetchall()

        query_obligacion = """
            INSERT INTO cartera_obligacionfinanciera (numero_referencia, cliente_id, persona_id) VALUES ('%s', '%s', '%s')
        """%(fila['Codigo referencia'], 1, id_[indice_fila][0])

        cursor.execute(query_obligacion)
        print('Success 🟢')
        connection.commit()

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
