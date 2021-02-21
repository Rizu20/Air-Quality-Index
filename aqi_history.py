import os
import sys
import urllib.request
from datetime import datetime
import json
import csv


def weather_request(lat,lon,start_date,end_date,api_key):
    start_date_unix=int(datetime.strptime(start_date,'%Y-%m-%d %H:%M:%S').timestamp())
    end_date_unix=int(datetime.strptime(end_date,'%Y-%m-%d %H:%M:%S').timestamp())
    url_string='http://api.openweathermap.org/data/2.5/air_pollution/history?lat='+str(lat)+'&lon='+str(lon)+'&start='+str(start_date_unix)+'&end='+str(end_date_unix)+'&appid='+api_key
    response=urllib.request.urlopen(url_string)
    if response.status==200:
        print("Response fetched successfully from API call")
        response_data=response.read().decode('utf-8')
        response_dict=json.loads(response_data)
        return response_dict
    else:
        print("Problem in fetching response to API call. Error code : {}".format(response.status))
        sys.exit()



def csv_file_write(response_dict):
    headers=['Response Time','AQI','CO','NO','NO2','O3','SO2','PM2_5','PM10','NH3']
    aqi_dict={1:'Good',2:'Fair',3:'Moderate',4:'Poor',5:'Very Poor'}

    with open(os.path.join(os.getcwd(),'output_history.csv'),'w',newline='') as f_out:
        csv_writer=csv.DictWriter(f_out,fieldnames=headers)
        csv_writer.writeheader()

        for i in response_dict['list']:
            response_time_unix=i["dt"]
            response_time=datetime.fromtimestamp(int(response_time_unix)).strftime('%Y-%m-%d %H:%M:%S')

            aqi=aqi_dict[i['main']['aqi']]

            co=i['components']['co']
            no=i['components']['no']
            no2=i['components']['no2']
            o3=i['components']['o3']
            so2=i['components']['so2']
            pm2_5=i['components']['pm2_5']
            pm10=i['components']['pm10']
            nh3=i['components']['nh3']

            row_dict={'Response Time':response_time,'AQI':aqi,'CO':co,'NO':no,'NO2':no2,'O3':o3,'SO2':so2,'PM2_5':pm2_5,'PM10':pm10,'NH3':nh3}

            csv_writer.writerow(row_dict)
    print("Response data from API call successfully written to CSV file.")
    


def main():
    lat=input("Please input Latitude of your location : ").strip()
    lon=input("Please input Longitude of your location : ").strip()
    start_date=input("Please input start date in format YYYY-MM-DD hh:mm:ss : ").strip()
    end_date=input("Please input end date in format YYYY-MM-DD hh:mm:ss : ").strip()
    api_key=input("Please input API key of your OpenWeatherMap account : ").strip()
    
    response_dict=weather_request(lat,lon,start_date,end_date,api_key)
    csv_file_write(response_dict)



main()

    

        

        

        
        

