import requests 
import json
import os

#denver woe_id : 2391279
def get_data():    
    c_code  = "44418"      # country code (e.g. "USA", "USA;CAN")    
    date    =["2020/4/1","2020/4/2","2020/4/3","2020/4/4","2020/4/5","2020/4/6","2020/4/7","2020/4/8","2020/4/9","2020/4/10","2020/4/11","2020/4/12","2020/4/13","2020/4/14","2020/4/15","2020/4/16","2020/4/17","2020/4/18","2020/4/19","2020/4/20","2020/4/21","2020/4/22","2020/4/23","2020/4/24","2020/4/25","2020/4/26","2020/4/27","2020/4/28","2020/4/29","2020/4/30","2020/4/31",]               # year (e.g. 2000) 
    for i in date:
        base_url    = "https://www.metaweather.com/api/location/{}/{}/"    
        request_url = base_url.format(c_code, i)    
        r = requests.get(request_url)    
        data = r.text        
        dict_list = json.loads(data) # decoding JSON file    
        print(dict_list[0]['max_temp'])    
    return(dict_list)


get_data()




