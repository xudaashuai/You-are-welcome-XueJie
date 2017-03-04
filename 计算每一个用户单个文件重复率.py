from bs4 import BeautifulSoup
import os
import datetime

path = "./data/剔除后/" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称

user_rate={
    #"user_id":[,,,,,]每个文件重复率
}

for file in files:
    f = open(path+'/'+file,encoding='utf-8')
    bs_file=BeautifulSoup(f, features="xml")
    one_day=datetime.timedelta(1)
    if bs_file.find_all('way').__len__() is 1:
        continue
    all_version=bs_file.find_all('way')
    for i in range(all_version.__len__()):
        user_id=all_version[i]['uid']
        file_rate=[]
        for j in range(all_version.__len__()):
            if i == j :
                continue
            same_num=0.0
            for nd in all_version[j].find_all('nd'):
                same=False
                for ind in all_version[i].find_all('nd'):
                    if nd['ref'] == ind['ref']:
                        same=True
                        break
                if same:
                    same_num+=1
            try:
                file_rate.append(same_num/all_version[j].find_all('nd').__len__())
            except:
                print(file,all_version[j])
        rate=sum(file_rate)/file_rate.__len__()
        if user_id in user_rate:
            user_rate[user_id].append(rate)
        else:
            user_rate[user_id] = [rate]
for x in user_rate.keys():
    user_rate[x]=sum(user_rate[x])/user_rate[x].__len__()
print(user_rate)
