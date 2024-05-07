import Connection.APIconnection as api
import pandas as pd
import datetime

from classes.Context import *
from  classes.User import *
from classes.Subservice import *
from classes.Interaction_sequence import *
from classes.Interaction import *


#api.set_default_repository("interaction_context")

df = pd.read_csv('sequences_df_prep_simulated_EN.csv', sep=",")
df["value_int"]=1
df_user = pd.read_csv('user_role.csv', sep=",")

grouped_df = df[['sd', 'user', 'turn','laborable',"numsteps"]].groupby(['sd', 'user', 'turn','laborable']).count().reset_index()

grouped_df['sd'] = grouped_df['sd'].astype("category")
grouped_df['user'] = grouped_df['user'].astype("category")

grouped_df['SD_id'] = grouped_df['sd'].cat.codes
grouped_df['user_id'] = grouped_df['user'].cat.codes

users_dic = {}
items_dic = {}

for i, row in grouped_df.iterrows():
    users_dic.setdefault(row["user"], row["user_id"])
    items_dic.setdefault(row["sd"], row["SD_id"])

d_context={"t1":41,"t2":42, 0:30,1:31,2:32,3:33,4:34,5:35,6:36}

Context(41, "shift","t1","Time").insert()
Context(42, "shift","t2","Time").insert()
Context(30, "dayofweek","0","Time").insert()
Context(31, "dayofweek","1","Time").insert()
Context(32, "dayofweek","2","Time").insert()
Context(33, "dayofweek","3","Time").insert()
Context(34, "dayofweek","4","Time").insert()
Context(35, "dayofweek","5","Time").insert()
Context(36, "dayofweek","6","Time").insert()


cont_user={}
role_user={}
for i, row in df_user.iterrows():
    cont_user[row.Role]=i
    role_user[row.User]=row.Role

for k, v in cont_user.items():
    Context(v, "role", k, "Identity").insert()

listUser=[]
for k,v in users_dic.items():
    listUser.append(User(v,k))
User.insertBatch(listUser)

listSubservice=[]

for k,v in items_dic.items():
    listSubservice.append(Subservice(v,k))
Subservice.insertBatch(listSubservice)

listInteractions=[]
compoundList=[]
batch = []

last=1
for i, row in df.iterrows():
    #initDate=str(datetime.datetime.fromtimestamp(row.initepoch/1000))
    #endDate=str(datetime.datetime.fromtimestamp(row.endepoch/1000))


    if row.turn in d_context:
        lc=[Context(d_context[row.turn], row.turn), Context(cont_user[role_user[row.user]], role_user[row.user]),Context(d_context[row.initdayofweek], row.initdayofweek)]

        inter = InteractionSequence(str(i),str(row.initepoch),str(row.endepoch), str(users_dic[row.user]), str(items_dic[row.sd]), [vars(ob) for ob in lc],str(row.value_int))
        print(vars(inter))

        for id_inter, element in enumerate(eval(row.interactionwu_prep)):
            individual=Interaction(id_inter+last,i, element,id_inter+1)
            batch.append(individual)
            if (len(batch)>1000):
                compoundList.append(batch[:])
                batch.clear()
        last+=id_inter+1

        listInteractions.append(inter)

compoundList.append(batch[:])
print("sending interactions to ontology")
InteractionSequence.insertBatch(listInteractions)
for b in compoundList:
        Interaction.insertBatch(b)
