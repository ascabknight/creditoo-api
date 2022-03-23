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
        cursor.execute("""SELECT id FROM cartera_persona""")
        id_persona = cursor.fetchall()

        for index, row in information.iterrows():

            query_obligacion = """
                INSERT INTO cartera_obligacionfinanciera (numero_referencia, cliente_id, persona_id) VALUES ('%s', '%s', '%s')
            """ % (row['codigo_ref'], 1, id_persona[index][0])

            cursor.execute(query_obligacion)
            print('Guardado ...', index, row['cedula'])
            connection.commit()

    except Exception as ex:
        print(ex)
    finally:
        connection.close()


if __name__ == '__main__':
    main()
