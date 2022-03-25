import pandas as pd
from os.path import dirname, join
import numpy as np


project_root = dirname(dirname(__file__))
client_info_path = join(project_root, 'datos/Database.csv')


client_info = pd.read_csv(client_info_path)
client_info_dataframe = pd.DataFrame()

client_info_dataframe['nombre_deudor'] = client_info['Nombre del Cliente']
client_info_dataframe['celular'] = client_info['Celular']
client_info_dataframe['codigo_ref'] = client_info['Llave']
client_info_dataframe['cedula'] = client_info['Cedula ']
client_info_dataframe['nombre_departamento'] = client_info['Nombre Departamento']
client_info_dataframe['nombre_ciudad'] = client_info['Nombre Ciudad']
client_info_dataframe['nombre_barrio'] = client_info['Nombre del Barrio']
client_info_dataframe['direccion'] = client_info['Direccion del Cliente']
client_info_dataframe['tramo'] = client_info['Tramo inicial']
client_info_dataframe['dias_mora'] = client_info['DIAS DE NO PAGO']
client_info_dataframe['saldo_mora'] = client_info['SALDO Total adeudado']
client_info_dataframe['total_pagar'] = client_info['Total a pagar']
client_info_dataframe['ultimo_pago'] = client_info['Fecha ultimo pago'].replace(np.nan, '2/12/1997')
client_info_dataframe['estado'] = client_info['Estado inicial']