import pandas as pd
from  classes.User import *
from classes.Context import *

Context(27, "role","undergraduate","Identity").insert()

last_record=27
u= pd.read_csv("ga4/newUsers.csv")
users_dic = {}
for i,row in u.iterrows():
    users_dic.setdefault(row["userid"], i+27)
print(users_dic)
listUser=[]
for k,v in users_dic.items():
    listUser.append(User(v,k))
print(listUser)
User.insertBatch(listUser)
