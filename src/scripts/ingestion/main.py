import pandas as pd
import psycopg2
import re
import json

#Conexion a base de datos
try:

    connection =  psycopg2.connect(
        host = "localhost",
        port = "5433",
        user = "postgres",
        password = 'cohen',
        database="pruebas"
    )
    
    print('Connection success 🟢')
    cursor = connection.cursor()

    
    #SOLO TRAEMOS LOS DATOS NO NULOS
    database = pd.read_csv('Database.csv').dropna()


    dataframe = pd.DataFrame()
    dataframe['Nombre deudor'] = database['Nombre del Cliente']
    dataframe['Celular'] =  database['Celular']
    dataframe['Llave'] = database['Llave']
    dataframe['Cedula'] = database['Cedula ']
    dataframe['Codigo ref'] = database['Llave']
    dataframe['Direccion del cliente'] = database['Nombre Ciudad'] + ' ' +  database['Direccion del Cliente']
    #Datos para cuentas por cobrar 
    dataframe['Tramo'] = database['Tramo inicial']
    dataframe['Dias en mora'] = database['DIAS DE NO PAGO']
    dataframe['Saldo en mora'] = database['SALDO Total adeudado']
    dataframe['Total a pagar'] = database['Total a pagar']
    dataframe['Fecha ultimo pago'] = database['Fecha ultimo pago']
    dataframe.set_index('Llave')
    
    
    print(dataframe.head(10).plot.scatter(y="Saldo en mora", x="Total a pagar"))
    
    for indice_fila, fila in dataframe.iterrows():  
        numeros = re.split("CE:|-|Ext:0", fila['Celular'])
        numeros = list(filter(str.strip, numeros))
        numero_concat = ''
        
        #OBLIGACIÓN FINANCIERA
        query_obligacion_financiera = """ INSERT INTO obligacion_financiera(DEUDOR, NUMERO_REFERENCIA) VALUES ('%s', '%s');
        """ % (fila['Nombre deudor'], fila['Codigo ref'])
        
        
        
        for numero in numeros:
            numero_concat += ',' + numero
    
            query = """
                INSERT INTO personas (CODIGO,PRIMER_NOMBRE, CEDULA, DIRECCION, NUMEROS) VALUES ('%s','%s', '%s', '%s', '%s'); 
                """ % (fila['Codigo ref'], fila['Nombre deudor'].split()[0], int(fila['Cedula']),fila['Direccion del cliente'], numero_concat)
        
    cursor.execute("SELECT * FROM obligacion_financiera")
    records = json.dumps(cursor.fetchall())
    print(records)
    connection.commit()
   
    
            
    


except Exception as ex:
    print(ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closed 🔴')
