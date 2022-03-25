from dataframes.clients import client_info_dataframe
from dataframes.emails import client_info_email_dataframe
import pandas as pd

information = pd.merge(client_info_dataframe, client_info_email_dataframe[['cedula', 'email']])