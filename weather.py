import requests 
import json
import os
import sqlite3
import matplotlib.pyplot as plt
#https://www.metaweather.com/api/
#denver woe_id : 2391279
# link that will help with dates https://docs.python.org/3/library/datetime.html
def get_data():    
    c_code  = "44418"         
    date    =["2020/4/1","2020/4/2","2020/4/3","2020/4/4","2020/4/5","2020/4/6","2020/4/7","2020/4/8","2020/4/9","2020/4/10","2020/4/11","2020/4/12","2020/4/13","2020/4/14","2020/4/15","2020/4/16","2020/4/17","2020/4/18","2020/4/19","2020/4/20","2020/4/21","2020/4/22","2020/4/23","2020/4/24","2020/4/25","2020/4/26","2020/4/27","2020/4/28","2020/4/29","2020/4/30","2020/4/31","2020/5/1","2020/5/2","2020/5/3","2020/5/4",
    "2020/5/5","2020/5/6","2020/5/7","2020/5/8","2020/5/9","2020/5/10","2020/5/11","2020/5/12","2020/5/13""2020/5/14","2020/5/15","2020/5/16","2020/5/17""2020/5/18","2020/5/19","2020/5/20","2020/5/21","2020/5/22","2020/5/23","2020/5/24","2020/5/25","2020/5/26","2020/5/27","2020/5/28","2020/5/29","2020/5/30"]               # year (e.g. 2000) 
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #conn = sqlite3.connect(dir_path + "/weather_data.db")
    #cur = conn.cursor()
    lst = []
    for i in date:
        base_url    = "https://www.metaweather.com/api/location/{}/{}/"    
        request_url = base_url.format(c_code, i)    
        r = requests.get(request_url)    
        data = r.text   
        #print(data)
        try:     
            dict_list = json.loads(data) # decoding JSON file 
        
            lst.append(dict_list[0]['max_temp']) 
        except:
            None  
        #print(dict_list[0]['max_temp'])  
        # return list of tuples with dates   
    print(lst)
    return(lst)

def database(lst):
       # for in range 25
       #create counter to see how many items have been added to the database
       #inner loop reads dict list from lst and adds 
       #range start at 0 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conn = sqlite3.connect(dir_path + "/weather_data.db")
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS weather ')
    cur.execute('CREATE TABLE weather(id INTEGER PRIMARY KEY, temperature FLOAT )')
    count = 0
    for g in range(0,4):
        for i in range(count,count+25):
            temp = lst[i]
            cur.execute('INSERT INTO weather(id,temperature) VALUES(?,?)',(i,temp))
        conn.commit()
        count+=25


            



lst=get_data()
database(lst)



