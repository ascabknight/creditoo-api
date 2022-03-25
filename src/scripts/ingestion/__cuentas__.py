import environ
import datetime
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


        now = datetime.datetime.now()
        current_date = now.strftime("%Y/%m/%d %H:%M:%S")

        cursor.execute('SELECT id  FROM cartera_obligacionfinanciera')
        id_obligacion = cursor.fetchall()

        for index, row in information.iterrows():
            saldo_mora = row['saldo_mora'].replace(',','')
            total_pagar = row['total_pagar'].replace(',','')

            query_cuentas = """
                INSERT INTO cartera_cuentasporcobrar (
                estado_obligacion, 
                fecha_ultimo_pago, 
                fecha_limite_pago,
                tramo, 
                dias_mora, 
                saldo_vencido, 
                total_pagar, 
                obligacion_id, 
                creado, 
                actualizado
                ) VALUES ('%s', '%s','%s', '%s','%s', '%s','%s', '%s','%s', '%s')
            """%(row['estado'], row['ultimo_pago'], '15/04/2022', row['tramo'], row['dias_mora'], saldo_mora, total_pagar, id_obligacion[index][0], current_date, current_date )

            cursor.execute(query_cuentas)
            print('Guardado...', index, row['cedula'])
            connection.commit()

    except Exception as ex:
        print(ex)
    finally:
        connection.close()


if __name__ == '__main__':
    main()