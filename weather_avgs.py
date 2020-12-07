    
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
cur.execute("SELECT weather.temperature FROM weather WHERE temperature >= 0")
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
for i in name_id[:31]:
    march_lst.append(i[0])
for i in march_lst:
    sum_march+=float(i)
for i in name_id[31:61]:
    april_lst.append(i[0])

for i in april_lst:
    sum_april+=float(i)
for i in name_id[61:89]:
    may_lst.append(i[0])
for i in may_lst:
    sum_may+=float(i)
for i in name_id[89:100]:
    june_lst.append(i[0])
for i in june_lst:
    sum_june+=float(i)
avg_march = sum_march / (len(march_lst))
avg_april = sum_april / (len(april_lst))
avg_may = sum_may / (len(may_lst))
avg_june = sum_june / (len(june_lst))
print(avg_march)
print(avg_april)
print(avg_may)
print(avg_june)