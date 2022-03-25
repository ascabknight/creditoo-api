import datetime
import environ
import psycopg2
from dataframes.merged import information

env = environ.Env()
# reading .env file
environ.Env.read_env()

DATABASE_HOST = env('DATABASE_HOST')
DATABASE_NAME = env('DATABASE_NAME')
DATABASE_USER = env('DATABASE_USER')
DATABASE_PASSWORD = env('DATABASE_PASSWORD')
DATABASE_PORT = env('DATABASE_PORT')

now = datetime.datetime.now()
current_date = now.strftime("%Y/%m/%d %H:%M:%S")


def main():
    try:
        connection = psycopg2.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME,
            port=DATABASE_PORT
        )

        print('Connection success!')
        cursor = connection.cursor()

        for index, row in information.iterrows():
            query_persona = """
                INSERT INTO cartera_persona (
                    numero_identificacion, 
                    tipo_identification, 
                    nombre_completo, 
                    telefono,
                    nombre_departamento,
                    nombre_ciudad,
                    nombre_barrio,
                    direccion, 
                    email, 
                    creado, 
                    actualizado
                    ) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
            """ % (row['cedula'], 'CC', row['nombre_deudor'], row['celular'], row['nombre_departamento'], row['nombre_ciudad'], row['nombre_barrio'], row['direccion'], row['email'], current_date, current_date)

            cursor.execute(query_persona)
            print('Guardado...', index, row['cedula'])
            connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()


if __name__ == '__main__':
    main()
