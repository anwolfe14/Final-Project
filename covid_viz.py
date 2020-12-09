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

dir_path = os.path.dirname(os.path.realpath(__file__))
conn = sqlite3.connect(dir_path + "/weather_data.db")
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

    
# for i in name_id[:31]:
#     march_lst.append(i[0])
# for i in march_lst:
#     sum_march+=float(i)
# for i in name_id[31:61]:
#     april_lst.append(i[0])

# for i in april_lst:
#     sum_april+=float(i)
# for i in name_id[61:89]:
#     may_lst.append(i[0])
# for i in may_lst:
#     sum_may+=float(i)
# for i in name_id[89:100]:
#     june_lst.append(i[0])
# for i in june_lst:
#     sum_june+=float(i)
avg_march = sum(march_lst) / (len(march_lst))
avg_april = sum(april_lst) / (len(april_lst))
avg_may = sum(may_lst) / (len(may_lst))
avg_june = sum(june_lst) / (len(june_lst))
print(avg_march)
print(avg_april)
print(avg_may)
print(avg_june)
avg_march_humid = sum(march_humid_lst) / (len(march_humid_lst))
avg_april_humid = sum(april_humid_lst) / (len(april_humid_lst))
avg_may_humid = sum(may_humid_lst) / (len(may_humid_lst))
avg_june_humid = sum(june_humid_lst) / (len(june_humid_lst))
print(avg_march_humid)
print(avg_april_humid)
print(avg_may_humid)
print(avg_june_humid)
#create a csv file that has headers as month names in temperature type
# columns months and the averages 

#look up box plot
#pyplot can be easier to use 
#add labels to x and y axis 
# name of csv file  
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
