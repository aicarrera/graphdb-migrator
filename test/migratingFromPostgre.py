import pandas as pd

from classes.Interaction import Interaction
from classes.User import *
from classes.Context import *
import re
from classes.Interaction_sequence import *
import time
import datetime


def useTimeLabel(current_hour):

    if 8 <= current_hour <= 13:
        return 't1'
    elif 14 <= current_hour <= 19:
        return 't2'
    else:
        return 't2'


def getDayOfWeek(dayOfWeek):
    dayOfWeek= int(dayOfWeek)
    if dayOfWeek == 1:
        return str(6)  # Sunday
    else:
        return str(dayOfWeek - 2)  # Monday to Saturday

filename="postgre/interactions_ult.csv"
#filename="ga4/02-06-2023.csv"

df = pd.read_csv(filename)

df_contexto = pd.read_csv("ga4/context_data_ontology.csv")
d_context = df_contexto.set_index('value')['id'].to_dict()

df_items = pd.read_csv("ga4/items_ontology.csv")
items_dic = df_items.set_index('name')['id'].to_dict()

df_users = pd.read_csv("ga4/users_ontology.csv")
users_dic = df_users.set_index('name')['id'].to_dict()
print(users_dic)
print(d_context)
print(items_dic)

df_users_role = pd.read_csv("ga4/newUsers.csv")
users_role_dic = df_users_role.set_index('userid')['role'].to_dict()
print(users_role_dic)

#Right now we are only filtering "Btn5" just to start ~ == not
dfFiltered = df[(df.element_id.str.startswith("btn5")) & (~df.element_id.str.startswith("btn5no"))]

'''
happy=3
meh=2
sad=1
'''
happy=1
meh=0.5
sad=0
dfFiltered["int_value"]=0
# In new version this should not be neccesary
dfFiltered.loc[dfFiltered.element_id.str.lower().str.startswith("btn5yes_"), 'int_value'] = 1
dfFiltered.loc[dfFiltered.element_id.str.lower().str.startswith("btn5happy_"), 'int_value'] = happy
dfFiltered.loc[dfFiltered.element_id.str.lower().str.startswith("btn5meh_"), 'int_value'] = meh
dfFiltered.loc[dfFiltered.element_id.str.lower().str.startswith("btn5sad_"), 'int_value'] = sad
pattern = re.compile(r'^btn5(?!sad|happy|meh|yes)[\w]')
# Use the pattern to filter the int_value column
matches=dfFiltered.element_id.str.lower().str.match(pattern)
dfFiltered.loc[matches, 'int_value'] = 1
dfFiltered.reset_index()
for i, row in dfFiltered.iterrows():
    print(row.user_id,row.element_id, row.int_value, row.related_data)
upload=True


if upload:
    #dfFiltered["int_value"] = (dfFiltered["int_value"] - -1) / (1 - -1)
    listInteractions = []
   # last_record = 1357
    #last=10577
    last_record = 2751
    last=11971
    compoundList=[]
    for i, row in dfFiltered.iterrows():
        role=users_role_dic[row.user_id]
        if role == "" or row.user_id not in users_dic:
            print(row.user_id)
            continue
        sd = row.related_data.split(",")[0].split(":")[1].strip('"').lower()
        if sd == "":
            sd = row.element_id.strip("btn5").replace("_click", "").lower()

        initdayofweek = "3" #getDayOfWeek(str(row.dayofweek))
        turn = "t1" #useTimeLabel(row.hour)

        print(i, row.element_id,row.user_id, role, row.epoch_time, sd, row.int_value, initdayofweek, turn)

        lc = [Context(d_context[turn], turn), Context(d_context[role], role),
              Context(d_context[initdayofweek], initdayofweek)]

        inter = InteractionSequence(str(i + last_record), str(row.epoch_time), str(row.epoch_time),
                                    str(users_dic[row.user_id]),
                                    str(items_dic[sd]), [vars(ob) for ob in lc], row.int_value)
        individual = Interaction(i + last, str(i + last_record), row.element_id.lower(), 1)
        compoundList.append(individual)
        print(vars(inter))
        listInteractions.append(inter)

    InteractionSequence.insertBatch(listInteractions)
    Interaction.insertBatch(compoundList)
