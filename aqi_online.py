import os
from urllib2 import urlopen
from datetime import datetime
import json
import csv

response=urlopen('http://api.openweathermap.org/data/2.5/air_pollution?lat=23.008598&lon=91.376448&appid=4df605e0ac7d6aaa401c9b6e8cf0b526')

if response.msg=='OK':
    response_status='Success'
    
    response_data=response.read()
    response_data=response_data.decode('utf-8')
    response_dict=json.loads(response_data)
    
    response_time_unix=response_dict['list'][0]["dt"]
    response_time=datetime.fromtimestamp(int(response_time_unix)).strftime('%Y-%m-%d %H:%M:%S')

    aqi_dict={1:'Good',2:'Fair',3:'Moderate',4:'Poor',5:'Very Poor'}
    aqi=aqi_dict[response_dict['list'][0]['main']['aqi']]

    co=response_dict['list'][0]['components']['co']
    no=response_dict['list'][0]['components']['no']
    no2=response_dict['list'][0]['components']['no2']
    o3=response_dict['list'][0]['components']['o3']
    so2=response_dict['list'][0]['components']['so2']
    pm2_5=response_dict['list'][0]['components']['pm2_5']
    pm10=response_dict['list'][0]['components']['pm10']
    nh3=response_dict['list'][0]['components']['nh3']



    headers=['Response Status','Response Time','AQI','CO','NO','NO2','O3','SO2','PM2_5','PM10','NH3']

    row_dict={'Response Status':response_status,'Response Time':response_time,'AQI':aqi,'CO':co,'NO':no,'NO2':no2,'O3':o3,'SO2':so2,'PM2_5':pm2_5,'PM10':pm10,'NH3':nh3}

    with open(r'/root/aqi/output.csv','a') as f_out:
        csv_writer=csv.DictWriter(f_out,fieldnames=headers)
        csv_writer.writerow(row_dict)
    
        
        

    
    

