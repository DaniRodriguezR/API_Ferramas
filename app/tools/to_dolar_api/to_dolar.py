import requests
import os

def fetch_dolar_data():

    # variables que tienen las variables de entorno de las credenciales para la api
    user = os.getenv('BANCO_CENTRAL_USER')
    password = os.getenv('PASSWORD_BANCO_CENTRAL')

    dolar_request = requests.get(f'https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user={user}&pass={password}&firstdate=2024-05-27&lastdate=2024-05-27&timeseries=F073.TCO.PRE.Z.D&function=GetSeries')

    if dolar_request.status_code == 200:
        data = dolar_request.json()
        series = data.get('Series', [])
        obs = series.get('Obs',[])
        for i in obs:
            value = i.get('value')
        return float(value) 

    else:
        print("Error al recopilar datos desde API Banco Central", dolar_request.status_code)
        return None