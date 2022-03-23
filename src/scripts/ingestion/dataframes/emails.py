import pandas as pd
from os.path import dirname, join


project_root = dirname(dirname(__file__))
client_info_email_path = join(project_root, 'datos/Emails.csv')

client_info_email = pd.read_csv(client_info_email_path)

client_info_email_dataframe = pd.DataFrame()
client_info_email_dataframe['cedula'] = client_info_email['Codigo del Cliente']
client_info_email_dataframe['email'] = client_info_email['Email'].replace(
    {"NOTIENE@CORREO.COM": None, "NOTIENE@GMAIL.COM": None})