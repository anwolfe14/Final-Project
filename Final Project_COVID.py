import csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sns
import requests
import json
import os
import datetime
import sqlite3

#Grab data from the following api: https://data.cdc.gov/resource/9mfq-cb36.json?$$app_token=vUO9dTV5pir6UBXemfD6uL8lZ. After this, create a database and inside that database, create a table named Covid with the following columns: date_id (integer), state (text), cases (integer), deaths (integer).Create a table named Dates with the following columns: date (text unique), date_id (Integer, primary key). Grab the data from the API and insert it into the table.
#Associate two tables with a key using the date_id. Lastly, make sure to only insert 25 data points per run. Please keep in mind that our Covid API changed at the last second and does not contain Colorado information anymore. Our presentation contained the information from Colorado Covid Cases. If you run our code now on Visual Studio, the create_table_Colorado() function will contain information from Montana, not Colorado, and thus have different data points.def create_table_Colorado():
def create_table_Colorado():
    api_2 = 'https://data.cdc.gov/resource/9mfq-cb36.json?$$app_token=vUO9dTV5pir6UBXemfD6uL8lZ'
    response_2 = (requests.get(api_2).json())
    dir_path = os.path.dirname(os.path.realpath(__file__))   
    conn = sqlite3.connect(dir_path + "/Covid_data.db")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Covid ("date_id" INTEGER UNIQUE, "state" TEXT, "cases" INTEGER, "deaths" INTEGER)')
    cur.execute('CREATE TABLE IF NOT EXISTS Dates ("date" TEXT UNIQUE, "date_id" INTEGER UNIQUE, PRIMARY KEY("date_id" AUTOINCREMENT))')
    cur.execute('SELECT date FROM Dates')
    date_lst = cur.fetchall()
    counting = len(date_lst)
    count = 0
    for state_data in response_2:
        if count ==25:
            break
        #We used Colorado (CO), not Montana (had to change to 'MO' two minutes before presenting as Colorado was deleted from API)
        if state_data['state'] == 'CO' and int(state_data['submission_date'][6]) > 2:
            try:
                cur.execute('SELECT date_id from Dates WHERE date = ?',(state_data['submission_date'],))
                date = cur.fetchone()[0]
            except:
                cur.execute('INSERT OR IGNORE INTO Dates (date) VALUES (?)', (state_data['submission_date'],))
                cur.execute('SELECT date_id from Dates WHERE date = ?',(state_data['submission_date'],))
                counting +=1
                date = cur.fetchone()[0]
            cur.execute('INSERT OR IGNORE INTO Covid (date_id,state,cases,deaths) VALUES (?,?,?,?)', (date, state_data['state'],state_data['new_case'],state_data['new_death']))
            if cur.rowcount ==1:   
                count+=1
    conn.commit()
    conn.close()

#Grab data from the following api: https://www.metaweather.com/api/location/. After this, create a table in the same database as the previous function named weather with the following parameters: "id" INTEGER UNIQUE PRIMARY KEY , "temperature" FLOAT, "date" TEXT, "humidity" FLOAT)'). Grab the temperature and humidity data from Colorado in the API during the 100 day span of March1-June8. Convert to Fahrenheit! Make sure to only submit 25 data points per run! Please keep in mind that our Covid API changed at the last second and does not contain Colorado information anymore. Our presentation contained the information from Colorado Covid Cases.If you run our code now on Visual Studio, the create_table_Colorado() function will contain information from Montana, not Colorado, and thus have different data points. 
def get_data():    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conn = sqlite3.connect(dir_path + "/Covid_data.db")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS weather("id" INTEGER UNIQUE PRIMARY KEY , "temperature" FLOAT, "date" TEXT, "humidity" FLOAT)')
    cursor = cur.execute('SELECT * FROM weather')
    count = len(cursor.fetchall())    
    c_code = "44418"  
    
    date =["2020/3/1","2020/3/2","2020/3/3","2020/3/4","2020/3/5","2020/3/6","2020/3/7","2020/3/8","2020/3/9","2020/3/10","2020/3/11","2020/3/12","2020/3/13","2020/3/14","2020/3/15","2020/3/16","2020/3/17","2020/3/18","2020/3/19","2020/3/20","2020/3/21","2020/3/22","2020/3/23","2020/3/24","2020/3/25","2020/3/26","2020/3/27","2020/3/28","2020/3/29","2020/3/30","2020/3/31",
    "2020/4/1","2020/4/2","2020/4/3","2020/4/4","2020/4/5","2020/4/6","2020/4/7","2020/4/8","2020/4/9","2020/4/10","2020/4/11","2020/4/12","2020/4/13","2020/4/14","2020/4/15","2020/4/16","2020/4/17","2020/4/18","2020/4/19","2020/4/20","2020/4/21","2020/4/22","2020/4/23","2020/4/24","2020/4/25","2020/4/26","2020/4/27","2020/4/28","2020/4/29","2020/4/30","2020/5/1","2020/5/2","2020/5/3","2020/5/4",
    "2020/5/5","2020/5/6","2020/5/7","2020/5/8","2020/5/9","2020/5/10","2020/5/11","2020/5/12","2020/5/13","2020/5/14","2020/5/15","2020/5/16","2020/5/17","2020/5/18","2020/5/19","2020/5/20","2020/5/21","2020/5/22","2020/5/23","2020/5/24","2020/5/25","2020/5/26","2020/5/27","2020/5/28","2020/5/29","2020/5/31","2020/6/1","2020/6/2","2020/6/3","2020/6/4","2020/6/5","2020/6/6","2020/6/7","2020/6/8","2020/6/9","2020/6/10","2020/6/11"] 
    
    lst_date = []
    lst_temps= []
    lst_humidity = []
    if count <= 75:
        for i in date[count:count+25]:
            
            lst =[]
            cur.execute('SELECT date FROM weather')
            relevant_data = cur.fetchall()
            for weather_data in relevant_data:
                lst.append(weather_data[0])
                
            if datetime.datetime.strptime(i, "%Y/%m/%d").strftime("%Y-%m-%d") in lst:
                print("found duplicate")
            else:
                base_url = "https://www.metaweather.com/api/location/{}/{}/"    
                request_url = base_url.format(c_code, i)    
                r = requests.get(request_url)    
                data = r.text   
               
                try:     
                    dict_list = json.loads(data) 
                
                    lst_temps.append(dict_list[0]['max_temp']) 
                    lst_date.append(dict_list[0]['applicable_date'])
                    lst_humidity.append(dict_list[0]['humidity'])
                except:
                    None
    else:
        for i in date[count:len(date)]:
            lst =[]
            cur.execute('SELECT date FROM weather')
            relevant_data = cur.fetchall()
            for weather_data in relevant_data:
                lst.append(weather_data[0])
            if datetime.datetime.strptime(i, "%Y/%m/%d").strftime("%Y-%m-%d") in lst:
                print("found duplicate")
            else:
                base_url = "https://www.metaweather.com/api/location/{}/{}/"    
                request_url = base_url.format(c_code, i)    
                r = requests.get(request_url)    
                data = r.text

                
                try:     
                    dict_list = json.loads(data) 
                
                    lst_temps.append(dict_list[0]['max_temp']) 
                    lst_date.append(dict_list[0]['applicable_date'])
                    lst_humidity.append(dict_list[0]['humidity'])
                except:
                    None    
    lst_tuple = list(zip(lst_temps,lst_date,lst_humidity))
    i = 1
    for tup in lst_tuple:
        try:
            temp = ((tup[0])*1.8) + 32
            date = tup[1]
            humid = tup[2] 
            cur.execute('INSERT INTO weather(id,temperature,date,humidity) VALUES(?,?,?,?)',(i+count,temp,date,humid))
            i+=1
        except:
            None
    conn.commit()
    return cur,conn
def main():
    create_table_Colorado()
    get_data()
if __name__ == "__main__":
     main()