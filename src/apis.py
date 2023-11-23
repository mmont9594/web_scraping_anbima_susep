#%%
import datetime
from typing import List
import requests
import pandas as pd
from io import StringIO


class InfoFromAnbima():
    def __init__(self, date: List[datetime.date], info_type: str):
        self.date = date
        self.info_type = info_type

    def get_data(self):
        if self.info_type == 'ETTJ':
            url = 'https://www.anbima.com.br/informacoes/est-termo/CZ-down.asp'
            dt = self.date
            payload = {"idioma": "US", "saida": "csv", "Dt_ref": dt.strftime("%d%m%Y")}
            response = requests.post(url=url, data=payload)
            ettj_parameters = pd.read_csv(StringIO(response.content.decode('utf-8')), sep=';', decimal='.', nrows=2)        
        return ettj_parameters


data_ettj = InfoFromAnbima(date=datetime.date(2023, 11, 22), info_type='ETTJ')
ettj_data = data_ettj.get_data()
print(ettj_data)