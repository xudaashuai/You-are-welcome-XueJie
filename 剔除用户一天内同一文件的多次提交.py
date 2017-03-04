from bs4 import BeautifulSoup
import os
import datetime

path = "./data/实验数据/" #文件夹目录
output_path = "./data/剔除后/" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称

user_times={}

for file in files:
    f = open(path+'/'+file,encoding='utf-8')
    bs_file=BeautifulSoup(f, features="xml")
    user_last_time={

    }
    one_day=datetime.timedelta(1)
    for x in bs_file.find_all('way'):

        if x.find_all('nd').__len__() is 0:
            x.extract()
            continue
        t=datetime.datetime.strptime(x['timestamp'],"%Y-%m-%dT%H:%M:%SZ")
        if x['user'] in user_last_time:
            if t-user_last_time[x['user']][0]<one_day:
                user_last_time[x['user']][1].extract()
                user_last_time[x['user']]=(t,x)
                print(file)
            else:
                user_last_time[x['user']]=(t,x)
        else:
            user_last_time[x['user']]=(t,x)
    html = bs_file.prettify("utf-8")
    with open(output_path+'/'+file, "wb") as file:
        file.write(html)
        file.flush()
        file.close()

