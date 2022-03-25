import environ
import psycopg2

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

        cursor.execute('ALTER SEQUENCE cartera_persona_id_seq RESTART WITH 100')
        print('Tabla cartera_persona alterada')
        connection.commit()
        
    except Exception as ex:
        print(ex)
    finally:
        connection.close()


if __name__ == '__main__':
    main()

