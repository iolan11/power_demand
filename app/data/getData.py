import requests
import json
from scipy.fft import fft, fftfreq
import numpy as np
from helper.json_processor import Json_processor as jp
import matplotlib.pyplot as plt

API_URL = "https://api.esios.ree.es/indicators/1293"
API_TOKEN = "385a57a79f04d3374703594cf82cc6c7b85bcc4a88115a8a0d776de2d6b7ae7e"

headers = {
        "Accept": "application/json; application/vnd.esios-api-v1+json",
        "Content-Type": "application/json",
        "x-api-key": API_TOKEN
    }
params = {
        "start_date": "2018-09-02 00:00:00",
        "end_date": "2018-10-06 00:00:00"
    }

class Get_Data:
    
    def __init__(self):
        self.jp_instance = jp()
    
    def get_dataset(self):
        
        #Recuperar dades de la api
        response = requests.get(API_URL, headers=headers, params=params)
    
        try:
            #comprobar l'status de la trucada
            response.raise_for_status()
            
            #recuperem la dada que necessitem de la resposta
            data = self.jp_instance.get_value_from_json('value', response.json())
            
            return self.fourier_transformation(data)
        
        except requests.exceptions.HTTPError as err:
            
            print('Error conecting to REE api')
    
    #Transformada de Fourier
    def fourier_transformation(self, data):
        
        #transformada de fourier
        fft_result = np.abs(fft(data)) # type: ignore
        
        #generem freqüències 
        freqs = fftfreq(len(data), 10)
        
        #Mostrar dades
        self.show_plots(fft_result, freqs, data)
        
        #Formatejar a json
        data_trans = [{"amplitude": fft_result[i], "freq": freqs[i]} for i in range(len(fft_result))]

        json_data = json.dumps(data_trans, indent=4)
        
        return json_data
    
    #Representar dades
    def show_plots(self, fft, freq, data):
        
        #Lllista de temps separats cada 10 min, que és el que ens retorna l'api de REE
        time = [i * 10 for i in range(len(fft))]
        
        """
        #Representar dades en funció del temps
        plt.plot(time, data)
        plt.xlabel('T(min)')
        plt.ylabel('A')
        plt.grid(True)
        plt.show()
        
        #Representar dades en funció de la freq
        plt.plot(freq, fft)
        plt.xlabel('Freq (Hz)')
        plt.ylabel('A')
        plt.grid(True)
        plt.show()
        """