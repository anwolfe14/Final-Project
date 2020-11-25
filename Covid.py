import csv
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import numpy as np
import seaborn as sns
import sqlite3
import json
from urllib.request import urlopen

df = pd.read_json(r'https://data.cdc.gov/resource/9mfq-cb36.json')
#Stat = df[['state','tot_cases']].groupby(['state']).sum()
#print(Stat)
#Stat2 = df[['state','tot_death']].groupby(['state']).sum()
#print(Stat2)
with urlopen("https://data.cdc.gov/resource/9mfq-cb36.json") as response:
    source = response.read()
data = json.loads(source)
#print(json.dumps(data, indent=2))
for item in data:
    for state in data[0]['state']:
        print(state)
#######

conn = sqlite3.connect('covid.db')

c = conn.cursor()
#c.execute('''DROP TABLE state''')

#c.execute('''CREATE TABLE state (
#    name TEXT,
 #   cases INT,
 #   death INT
#)''')
#name = 'Colorado'
#cases = 0
#death = 0

#c.execute('''INSERT INTO state VALUES(?,?,?)''',(df[['state','tot_cases','tot_death']]))
conn.commit()

c.execute('''SELECT * FROM state''')
results = c.fetchall()
print(results)

conn.close()