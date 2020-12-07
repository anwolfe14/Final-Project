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
    date    =["2020/3/1","2020/3/2","2020/3/3","2020/3/4","2020/3/5","2020/3/6","2020/3/7","2020/3/8","2020/3/9","2020/3/10","2020/3/11","2020/3/12","2020/3/13","2020/3/14","2020/3/15","2020/3/16","2020/3/17","2020/3/18","2020/3/19","2020/3/20","2020/3/21","2020/3/22","2020/3/23","2020/3/24","2020/3/25","2020/3/26","2020/3/27","2020/3/28","2020/3/29","2020/3/30","2020/3/31",
    "2020/4/1","2020/4/2","2020/4/3","2020/4/4","2020/4/5","2020/4/6","2020/4/7","2020/4/8","2020/4/9","2020/4/10","2020/4/11","2020/4/12","2020/4/13","2020/4/14","2020/4/15","2020/4/16","2020/4/17","2020/4/18","2020/4/19","2020/4/20","2020/4/21","2020/4/22","2020/4/23","2020/4/24","2020/4/25","2020/4/26","2020/4/27","2020/4/28","2020/4/29","2020/4/30","2020/4/31","2020/5/1","2020/5/2","2020/5/3","2020/5/4",
    "2020/5/5","2020/5/6","2020/5/7","2020/5/8","2020/5/9","2020/5/10","2020/5/11","2020/5/12","2020/5/13","2020/5/14","2020/5/15","2020/5/16","2020/5/17""2020/5/18","2020/5/19","2020/5/20","2020/5/21","2020/5/22","2020/5/23","2020/5/24","2020/5/25","2020/5/26","2020/5/27","2020/5/28","2020/5/29","2020/5/31","2020/6/1","2020/6/2","2020/6/3","2020/6/4","2020/6/5","2020/6/6","2020/6/7","2020/6/8","2020/6/9","2020/6/10","2020/6/11"]               # year (e.g. 2000) 
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    #conn = sqlite3.connect(dir_path + "/weather_data.db")
    #cur = conn.cursor()
    lst = []
    lst2= []
    
    for i in date:
        base_url    = "https://www.metaweather.com/api/location/{}/{}/"    
        request_url = base_url.format(c_code, i)    
        r = requests.get(request_url)    
        data = r.text   
        #print(data)
        try:     
            dict_list = json.loads(data) # decoding JSON file 
        
            lst.append(dict_list[0]['max_temp']) 
            lst2.append(dict_list[0]['applicable_date'])
        except:
            None  
        #print(dict_list[0]['max_temp'])  
        # return list of tuples with dates   
    lst_tuple = list(zip(lst,lst2))
    #print(lst)
    #print(lst2)
    #print(lst_tuple)
    return(lst_tuple)

def database(lst_tuple):
       # for in range 25
       #create counter to see how many items have been added to the database
       #inner loop reads dict list from lst and adds 
       #range start at 0 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conn = sqlite3.connect(dir_path + "/weather_data.db")
    cur = conn.cursor()
    #cur.execute('DROP TABLE IF EXISTS weather ')
    #cur.execute('DROP TABLE weather')
    cur.execute('CREATE TABLE IF NOT EXISTS weather(id INTEGER PRIMARY KEY, temperature FLOAT, date TEXT )')
    count = 0
    for g in range(0,4):
        for i in range(count,count+25):
            temp = ((lst_tuple[i][0])*1.8) + 32
            date = lst_tuple[i][1]
            cur.execute('INSERT INTO weather(id,temperature,date) VALUES(?,?,?)',(i,temp,date))
        conn.commit()
        count+=25
        #if count > 25:
            #print("There should only be 25 entries")
            #break
        print(g)
    print("done")
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
    return cur,conn

#def averages(cur,conn):
    #conn.execute("SELECT * FROM weather WHERE date = ?")
    #print(conn.fetchall())

            



lst=get_data()
database(lst)
#conn = database(lst)
#cur = database(lst)
#averages(cur,conn)


