# Air-Quality-Index
This script is a test of AQI measurement using OpenWeatherMap API.

aqi_history_backup.py places a single call to fetch hourly AQI data for a certain time period and creates a csv file. Later, charts can be created from the csv file using Excel. There are some problem with default Excel line chart (hourly line chart and placement of horizontal axis)
https://imgur.com/VZrvvrb

aqi_online.py places a single call to fetch only the latest AQI data for only one hour and update output csv file. But can be run with cronjob and scheduled to run at every hour to create online csv file.
