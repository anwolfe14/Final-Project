import requests 
import json
import os
import sqlite3
import datetime
import matplotlib.pyplot as plt
#https://www.metaweather.com/api/
#denver woe_id : 2391279
# This was used to solve some of the fomrating from the api https://docs.python.org/3/library/datetime.html
def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conn = sqlite3.connect(dir_path + "/weather_data.db")
    cur = conn.cursor()
    #cur.execute('DROP TABLE IF EXISTS weather ')
    #cur.execute('DROP TABLE weather')
    cur.execute('CREATE TABLE IF NOT EXISTS weather(id INTEGER PRIMARY KEY, temperature FLOAT, date TEXT )')
    cursor = cur.execute('SELECT * FROM weather')
    count = len(cursor.fetchall())    
    c_code  = "44418"  
    #date = ["2020/3/1","2020/3/2","2020/3/3"]     
    date    =["2020/3/1","2020/3/2","2020/3/3","2020/3/4","2020/3/5","2020/3/6","2020/3/7","2020/3/8","2020/3/9","2020/3/10","2020/3/11","2020/3/12","2020/3/13","2020/3/14","2020/3/15","2020/3/16","2020/3/17","2020/3/18","2020/3/19","2020/3/20","2020/3/21","2020/3/22","2020/3/23","2020/3/24","2020/3/25","2020/3/26","2020/3/27","2020/3/28","2020/3/29","2020/3/30","2020/3/31",
    "2020/4/1","2020/4/2","2020/4/3","2020/4/4","2020/4/5","2020/4/6","2020/4/7","2020/4/8","2020/4/9","2020/4/10","2020/4/11","2020/4/12","2020/4/13","2020/4/14","2020/4/15","2020/4/16","2020/4/17","2020/4/18","2020/4/19","2020/4/20","2020/4/21","2020/4/22","2020/4/23","2020/4/24","2020/4/25","2020/4/26","2020/4/27","2020/4/28","2020/4/29","2020/4/30","2020/5/1","2020/5/2","2020/5/3","2020/5/4",
    "2020/5/5","2020/5/6","2020/5/7","2020/5/8","2020/5/9","2020/5/10","2020/5/11","2020/5/12","2020/5/13","2020/5/14","2020/5/15","2020/5/16","2020/5/17","2020/5/18","2020/5/19","2020/5/20","2020/5/21","2020/5/22","2020/5/23","2020/5/24","2020/5/25","2020/5/26","2020/5/27","2020/5/28","2020/5/29","2020/5/31","2020/6/1","2020/6/2","2020/6/3","2020/6/4","2020/6/5","2020/6/6","2020/6/7","2020/6/8","2020/6/9","2020/6/10","2020/6/11"] 
    #add more dates to date lst              # year (e.g. 2000) 

    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #conn = sqlite3.connect(dir_path + "/weather_data.db")
    #cur = conn.cursor()
    lst_date = []
    lst_temps= []
    if count <= 75:
        for i in date[count:count+25]:
            #print(i)
            lst =[]
            cur.execute('SELECT date FROM weather')
            relevant_data = cur.fetchall()
            for weather_data in relevant_data:
                lst.append(weather_data[0])
                #print(weather_data[0])
            #print('#########')
            #print(datetime.datetime.strptime(i, "%Y/%m/%d").strftime("%Y-%m-%d"))
            if datetime.datetime.strptime(i, "%Y/%m/%d").strftime("%Y-%m-%d") in lst:
                print("found duplicate")
            else:
                base_url = "https://www.metaweather.com/api/location/{}/{}/"    
                request_url = base_url.format(c_code, i)    
                r = requests.get(request_url)    
                data = r.text   
                #print(data)
                try:     
                    dict_list = json.loads(data) # decoding JSON file 
                
                    lst_temps.append(dict_list[0]['max_temp']) 
                    lst_date.append(dict_list[0]['applicable_date'])
                except:
                    None#print(data)
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
                base_url    = "https://www.metaweather.com/api/location/{}/{}/"    
                request_url = base_url.format(c_code, i)    
                r = requests.get(request_url)    
                data = r.text

                #print(data)
                try:     
                    dict_list = json.loads(data) # decoding JSON file 
                
                    lst_temps.append(dict_list[0]['max_temp']) 
                    lst_date.append(dict_list[0]['applicable_date'])
                except:
                    None  
        #print(dict_list[0]['max_temp'])  
        # return list of tuples with dates   
    lst_tuple = list(zip(lst_temps,lst_date))
    #print(lst)
    #print(lst2)
    #print(lst_tuple)
    #return(lst_tuple)


       # for in range 25
       #create counter to see how many items have been added to the database
       #inner loop reads dict list from lst and adds 
       #range start at 0 
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # conn = sqlite3.connect(dir_path + "/weather_data.db")
    # cur = conn.cursor()
    # #cur.execute('DROP TABLE IF EXISTS weather ')
    # cur.execute('CREATE TABLE IF NOT EXISTS weather(id INTEGER PRIMARY KEY, temperature FLOAT, date TEXT )')
    # cursor = cur.execute('SELECT * FROM weather')
    # count = len(cursor.fetchall())
    # print(count)
    i = 0
    for tup in lst_tuple:
        try:
            #print(tuple)
            temp = ((tup[0])*1.8) + 32
            date = tup[1]
            cur.execute('INSERT INTO weather(id,temperature,date) VALUES(?,?,?)',(i+count,temp,date))
            i+=1
        except:
            None
    conn.commit()
    ###new start###
    # count = 0 
    # lst =[]
    # relevant_data = cur.execute('SELECT date FROM weather')
    # for weather_data in relevant_data:
    #     lst.append(weather[0])
    # for weather_data in lst_tuple:
    #     if count == 25:
    #         break
    #     if weather_data in lst:
    #         continue
    ###new end###
    ### How I had it start ### 
    #count = 0
    #for g in range(0,4):
        #for i in range(count,count+25):
            #temp = ((lst_tuple[i][0])*1.8) + 32
            #date = lst_tuple[i][1]
            #cur.execute('INSERT INTO weather(id,temperature,date) VALUES(?,?,?)',(i,temp,date))
        #conn.commit()
        #count+=25
        #if count > 25:
            #print("There should only be 25 entries")
            #break
        #print(g)
    #print("done")
    ### How I had it end ### 
    return cur,conn
           

get_data()
#database(lst)
#conn = database(lst)
#cur = database(lst)
#averages(cur,conn)


