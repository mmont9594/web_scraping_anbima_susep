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
        elif self.info_type == 'VNA':
            url = 'https://www.anbima.com.br/informacoes/vna/vna-down.asp'
            dt = self.date
            payload = {"Data": dt.strftime("%d%m%Y"), "saida": "csv", "idioma": "US"}
            response = requests.post(url=url, data=payload)
            vna_parameters = pd.read_csv(StringIO(response.content.decode('latin-1')), sep=";", decimal=",", skiprows=7)        
            return vna_parameters
        elif self.info_type == 'YTM':
            dt = self.date
            url = 'https://www.anbima.com.br/informacoes/merc-sec/arqs/ms' + dt.strftime("%y%m%d") + '.txt'
            response = requests.get(url=url)
            ymt_parameters = pd.read_csv(StringIO(response.content.decode('latin-1')), sep="@", decimal=",", skiprows=2)    
            return ymt_parameters
            
