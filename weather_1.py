import requests 
import json
import os
import sqlite3
import datetime
import matplotlib.pyplot as plt

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