from bs4 import BeautifulSoup
import os
import datetime

path = "./data/剔除后/" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称

user_time={}

for file in files:
    f = open(path+'/'+file,encoding='utf-8')
    bs_file=BeautifulSoup(f, features="xml")
    one_day=datetime.timedelta(1)
    for x in bs_file.find_all('way'):
        user_id=x['uid']
        t=datetime.datetime.strptime(x['timestamp'],"%Y-%m-%dT%H:%M:%SZ")
        if user_id in user_time.keys() and user_time[user_id]<t:
            continue
        else:
            user_time[user_id]=t

print(user_time)
