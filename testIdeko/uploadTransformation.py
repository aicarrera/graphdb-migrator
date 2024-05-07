from classes.Subservice import *
from classes.Service import *
from classes.Context import *
from classes.Interaction_sequence import *
from classes.Interaction import *
from functions_helper import *


import pandas as pd
# Set options to display all columns and rows without truncation
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_rows', 70)
pd.set_option('display.expand_frame_repr', True)  # Prevent line wrapping of long rows
pd.set_option('display.width', 400)

df = pd.read_csv('processedSequences.csv', sep=",")
dftransformations= df[df["event_general"] == "selectTransformations_change"]
print(dftransformations.head(100))

dtransformationGroup = dftransformations[["event_label", "sequence_id"]].groupby(["event_label"]).count().reset_index()

dicService={}
dicSubservice={}
id=300
listaTransformation=[]
for i, row in dtransformationGroup.iterrows():
    listaTransformation.append(Subservice(id, row["event_label"].replace(",","-")))
    dicSubservice[row["event_label"]]=id
    id+=1

listService = []
index=300
listService.append(Service(index, "transformation_execution", None, [vars(ob) for ob in listaTransformation]))
index += 1

Service.insertBatch(listService)

# *****InsertInteractions ******
contextDic = {"t1": 41, "t2": 42}
listInteractions=[]
compoundList=[]
# get users
users_dic = getUsersDic(getRoles())

inter_seq_index = 3000
for i, row in dftransformations.iterrows():
    lc = [Context(contextDic[row["shift"]], row["shift"]),
          Context(users_dic[row.user_id]["idrole"], users_dic[row.user_id]["role"])]
    inter = InteractionSequence(str(inter_seq_index), str(getTimestamp(row.start_date)),
                                str(getTimestamp(row.end_date)), str(users_dic[row.user_id]["id"]),
                                str(dicSubservice[row.event_label]), [vars(ob) for ob in lc], str(1))
    individual = Interaction(inter_seq_index, str(inter_seq_index), row.unifiedEvent, 1)
    compoundList.append(individual)
    inter_seq_index += 1
    print(vars(inter))

    listInteractions.append(inter)

upload_batches(listInteractions, compoundList)
