import csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sns
import requests
import json
import os
import sqlite3

#this file finds the monthly temperature averages and monthly humidity averages in Colorado 
dir_path = os.path.dirname(os.path.realpath(__file__))   
conn = sqlite3.connect(dir_path + "/Covid_data.db")#opens database
cur = conn.cursor()
cur.execute("SELECT * FROM weather WHERE temperature >= 0") #selects positive temperatures from the weather table
name_id = cur.fetchall()
march_lst = [] #these lists will store the temperatures for each month
april_lst = []
may_lst = []
june_lst = []
avg_march = 0
sum_march = 0
avg_april = 0
sum_april = 0
avg_may = 0
sum_may = 0
avg_june = 0
sum_june = 0
for tup in name_id: #this "for" statement takes the full date from the weather table and selects each month off of a numerical value.
    date = tup[2]
    date_lst = date.split('-')
    temperature = float(tup[1])
    month = int(date_lst[1])
    if month == 3: #selects march
        march_lst.append(temperature)
    elif month == 4: #selects april
        april_lst.append(temperature)
    elif month == 5:#selects may
        may_lst.append(temperature)
    elif month == 6: #selects june
        june_lst.append(temperature)
march_humid_lst = [] #these lists will store humidity values for each month
april_humid_lst = []
may_humid_lst = []
june_humid_lst = []
cur.execute("SELECT * FROM weather WHERE humidity >= 0")
name_id = cur.fetchall()
for tup in name_id: #this "for" statement takes the full date from the weather table and selects each month off of a numerical value.
    date = tup[2]
    date_lst = date.split('-')
    temperature = float(tup[3])
    month = int(date_lst[1])
    if month == 3:#selects march
        march_humid_lst.append(temperature)
    elif month == 4:#selects april
        april_humid_lst.append(temperature)
    elif month == 5:#selects may
        may_humid_lst.append(temperature)
    elif month == 6:#selects june
        june_humid_lst.append(temperature)
###this section calculates the averages for both temperature and humidity for each month 
avg_march = sum(march_lst) / (len(march_lst)) #these calculate the average temperature for each month
avg_april = sum(april_lst) / (len(april_lst))
avg_may = sum(may_lst) / (len(may_lst))
avg_june = sum(june_lst) / (len(june_lst))

avg_march_humid = sum(march_humid_lst) / (len(march_humid_lst)) #these calculate the average humidity for each month
avg_april_humid = sum(april_humid_lst) / (len(april_humid_lst))
avg_may_humid = sum(may_humid_lst) / (len(may_humid_lst))
avg_june_humid = sum(june_humid_lst) / (len(june_humid_lst))

###This section will store the calculated averages and store them into a csv file
filename = "weather_avgs.csv"
title = ['Average monthly temperatures in fahrenheit for ']
fields = ['March,' 'April,' 'May,' 'June']
rows = ([avg_march],[avg_april],[avg_may],[avg_june])
march = (avg_march)
april = (avg_april)
may = (avg_may)
june = (avg_june)
humid_march =(avg_march_humid)
humid_april =(avg_april_humid)
humid_may =(avg_may_humid)
humid_june =(avg_june_humid)
month_name = ['Type','March', 'April', 'May', 'June']
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    #csvwriter = csv.writer(csvfile)     
    csvwriter = csv.DictWriter(csvfile,fieldnames=month_name)  
    csvwriter.writeheader()
    #csvwriter.writerow("Monthly Temperature Averages in Fahrenheit")
    csvwriter.writerow({'Type':"temperature averages",'March':round(march),'April':round(april),'May':round(may),'June':round(june)})
    csvwriter.writerow({'Type':"humidity averages",'March':round(humid_march),'April':round(humid_april),'May':round(humid_may),'June':round(humid_june)})
    
###This section creates a line chart for the average temperature and humidity for each month
plt.title("Monthly Average Temperatures in Colorado ")
plt.xlabel("Months")
plt.ylabel("Temperature in Fahrenheit")
dev_x = ['March','April','May','June']
dev_y =[avg_march,avg_april,avg_may,avg_june]
dev_y2 =[avg_march_humid,avg_april_humid,avg_may_humid,avg_june_humid]
plt.plot(dev_x, dev_y, label='Temperatures')
plt.plot(dev_x, dev_y2, 'k--', label='Humidity')
plt.legend()
plt.grid(True)
plt.show()

cur.execute("SELECT Covid.cases FROM Covid WHERE cases >= 0")
name_id = cur.fetchall()
march_covid = []
march_sum = 0
march_average = 0
april_covid = []
april_sum = 0
april_average = 0
june_covid = []
june_sum = 0
june_average = 0
may_covid = []
may_sum = 0
may_average = 0
for i in (name_id[:30]):
    march_covid.append(i[0])
for i in march_covid:
    march_sum+=i
march_average = march_sum / len(march_covid)
for i in (name_id[31:61]):
    april_covid.append(i[0])
for i in april_covid:
    april_sum+=i
april_average = april_sum / len(april_covid)
for i in (name_id[62:92]):
    may_covid.append(i[0])
for i in may_covid:
    may_sum+=i
may_average = may_sum / len(may_covid)
for i in (name_id[93:100]):
    june_covid.append(i[0])
for i in june_covid:
    june_sum+=i
june_average = june_sum / len(june_covid)

cur.execute("SELECT Covid.deaths FROM Covid WHERE deaths >= 0")
name_id_death = cur.fetchall()
march_covid_death = []
march_sum_death = 0
march_average_death = 0
april_covid_death = []
april_sum_death = 0
april_average_death = 0
june_covid_death = []
june_sum_death = 0
june_average_death = 0
may_covid_death = []
may_sum_death = 0
may_average_death = 0
for i in (name_id_death[:30]):
    march_covid_death.append(i[0])
for i in march_covid:
    march_sum+=i
march_average_death = march_sum_death / len(march_covid_death)
for i in (name_id_death[31:61]):
    april_covid_death.append(i[0])
for i in april_covid_death:
    april_sum_death+=i
april_average_death = april_sum_death / len(april_covid_death)
for i in (name_id_death[62:92]):
    may_covid_death.append(i[0])
for i in may_covid_death:
    may_sum_death+=i
may_average_death = may_sum_death / len(may_covid_death)
for i in (name_id_death[93:100]):
    june_covid_death.append(i[0])
for i in june_covid_death:
    june_sum_death+=i
june_average_death = june_sum_death / len(june_covid_death)

    
plt.title("Covid Cases Colorado")
plt.xlabel("Months")
plt.ylabel("Confirmed Cases")
dev_x = ['March','April','May','June']
dev_y =[march_average,april_average,may_average,june_average]
dev_y2 =[march_average_death,april_average_death,may_average_death,june_average_death]
plt.plot(dev_x, dev_y, label='Average Cases per day')
plt.plot(dev_x, dev_y2, label='Average Deaths per day')
plt.legend()
plt.grid()
plt.show()
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    #csvwriter = csv.writer(csvfile)     
    csvwriter = csv.DictWriter(csvfile,fieldnames=month_name)  
    csvwriter.writeheader()
    #csvwriter.writerow("Monthly Temperature Averages in Fahrenheit")
    csvwriter.writerow({'Type':"Temperature Averages",'March':round(march),'April':round(april),'May':round(may),'June':round(june)})
    csvwriter.writerow({'Type':"Humidity Averages",'March':round(humid_march),'April':round(humid_april),'May':round(humid_may),'June':round(humid_june)})
    csvwriter.writerow({'Type':"Average Covid Cases Per Day",'March':round(march_average),'April':round(april_average),'May':round(may_average),'June':round(june_average)})
    csvwriter.writerow({'Type':"Average Covid Deaths Per Day",'March':round(march_average_death),'April':round(april_average_death),'May':round(may_average_death),'June':round(june_average_death)})



