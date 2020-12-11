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
#Select data from the weather and Covid table. From these tables calculate the average temperature (for each month), the average humidity (for each month), the average number of Covid-19 cases per day (for each month), and the average number of Covid-19 deaths per day (for each month). Using this information, create three subplots and one bar graph. One subplot will contain the averages from temperature and humidity, the second subplot will contain the averages from cases and deaths, and the third subplot will contain the total number of Covid cases and deaths per month (for each month). The fourth visualization wil be a bar graph comparing the average number of deaths per day due to Covid for each month. Lastly, insert all of the data calculated into a CSV file.Please keep in mind that our Covid API changed at the last second and does not contain Colorado information anymore. Our presentation contained the information from Colorado Covid Cases. If you run our code now on Visual Studio, the create_table_Colorado() function will contain information from Montana, not Colorado, and thus have different data points. 
dir_path = os.path.dirname(os.path.realpath(__file__))   
conn = sqlite3.connect(dir_path + "/Covid_data.db")
cur = conn.cursor()
cur.execute("SELECT * FROM weather WHERE temperature >= 0")
name_id = cur.fetchall()
march_lst = []
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
for tup in name_id:
    date = tup[2]
    date_lst = date.split('-')
    temperature = float(tup[1])
    month = int(date_lst[1])
    if month == 3:
        march_lst.append(temperature)
    elif month == 4:
        april_lst.append(temperature)
    elif month == 5:
        may_lst.append(temperature)
    elif month == 6:
        june_lst.append(temperature)
march_humid_lst = []
april_humid_lst = []
may_humid_lst = []
june_humid_lst = []
cur.execute("SELECT * FROM weather WHERE humidity >= 0")
name_id = cur.fetchall()
for tup in name_id:
    date = tup[2]
    date_lst = date.split('-')
    temperature = float(tup[3])
    month = int(date_lst[1])
    if month == 3:
        march_humid_lst.append(temperature)
    elif month == 4:
        april_humid_lst.append(temperature)
    elif month == 5:
        may_humid_lst.append(temperature)
    elif month == 6:
        june_humid_lst.append(temperature)
avg_march = sum(march_lst) / (len(march_lst))
avg_april = sum(april_lst) / (len(april_lst))
avg_may = sum(may_lst) / (len(may_lst))
avg_june = sum(june_lst) / (len(june_lst))

avg_march_humid = sum(march_humid_lst) / (len(march_humid_lst))
avg_april_humid = sum(april_humid_lst) / (len(april_humid_lst))
avg_may_humid = sum(may_humid_lst) / (len(may_humid_lst))
avg_june_humid = sum(june_humid_lst) / (len(june_humid_lst))

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

plt.title("Average Covid Deaths")
plt.xlabel("Months")
plt.ylabel("Average Covid Deaths per day")
dev_x = ['March','April','May','June']
dev_y =[march_average_death,april_average_death,may_average_death,june_average_death]
plt.bar(dev_x, dev_y, label='Average Covid Deaths per day', color = 'red')
plt.legend()
plt.grid()
plt.show()

plt.title("Covid-19 by Month")
plt.xlabel("Months")
dev_x = ['March','April','May','June']
dev_y =[march_sum,april_sum,may_sum,june_sum]
dev_y2 =[march_sum_death,april_sum_death,may_sum_death,june_sum_death]
plt.plot(dev_x, dev_y, 'r-',label='Number of Covid Cases per Month')
plt.plot(dev_x, dev_y2, 'g-',label='Number of Covid Deaths per Month')
plt.legend()
plt.grid()
plt.show()

plt.title("Covid Cases Colorado")
plt.xlabel("Months")
plt.ylabel("Confirmed Cases")
dev_x = ['March','April','May','June']
dev_y =[march_average,april_average,may_average,june_average]
dev_y2 =[march_average_death,april_average_death,may_average_death,june_average_death]
plt.plot(dev_x, dev_y,'r-', label='Average Cases per day')
plt.plot(dev_x, dev_y2, 'g-',label='Average Deaths per day')
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



