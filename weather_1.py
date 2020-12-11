import requests 
import json
import os
import sqlite3
import datetime
import matplotlib.pyplot as plt
#Once all of the databases are correct and have 100 data points in each table, use the join operator on SQL to create a new table named Covid_Weather that contains date_id, state, cases, deaths, temperature, and humidity from the tables Covid and weather. Please keep in mind that our Covid API changed at the last second and does not contain Colorado information anymore. Our presentation contained the information from Colorado Covid Cases. If you run our code now on Visual Studio, the create_table_Colorado() function will contain information from Montana, not Colorado, and thus have different data points. 
def joining():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conn = sqlite3.connect(dir_path + "/Covid_data.db")
    cur = conn.cursor()
    cur.execute("Create TABLE Covid_weather as SELECT date_id, state, cases, deaths, temperature,humidity FROM weather JOIN Covid WHERE Covid.date_id = weather.id")
    conn.commit()
def main():
    joining()
if __name__ == "__main__":
     main()