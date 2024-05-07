import pandas as pd
from classes.Context import *
from classes.User import *
from classes.Subservice import *
from classes.Service import *
from classes.Interaction_sequence import *
from classes.Interaction import *
from functions_helper import *

# Set options to display all columns and rows without truncation
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.max_rows', 70)
pd.set_option('display.expand_frame_repr', True)  # Prevent line wrapping of long rows
pd.set_option('display.width', 400)

df = pd.read_csv('processedSequences.csv', sep=",")
print(df.columns)

dfSignals= df[df["event_general"] == "selectSignals_change"][["event_general","option","event_name","event_label"]].groupby(["event_general","event_label"]).count().reset_index()
print(dfSignals.head(100))

dfTransformations= df[df["event_general"] == "selectTransformations_change"][["event_general","option","event_name","event_label"]].groupby(["event_general","event_label"]).count().reset_index()
print(dfTransformations.head(100))

dfIndicator= df[df["event_general"] == "selectIndicators_change"][["event_general","option","event_name","event_label"]].groupby(["event_general","event_label"]).count().reset_index()
print(dfIndicator.head(100))

dfList = pd.read_csv('processedSequencesList.csv')

if False:
    df_users= df[["user_id","sequence_id"]].groupby(["user_id"]).count().reset_index()
    df_users.user_id.to_csv("users.csv")


upload = True
if  upload:
    for role,id in roles.items():
        Context(id, "role",role,"Identity").insert()


    Context(41, "shift","t1","Time").insert()
    Context(42, "shift","t2","Time").insert()
    contextDic={"t1":41,"t2":42}
    #*****Insert ServicesMachines*****
    df["page_location"]= df["page_location"].str.replace("http://","").str.split(".").str[-2:].str.join(".")
    df_pages= df[["page_location", "machine", "sequence_id"]].groupby(["page_location", "machine"]).count().reset_index()
    location=""
    index=0
    dicService={}
    dicSubservice={}
    index_subservice=200
    for i, row in df_pages.iterrows():
        listaMachine= dicService.setdefault(row["page_location"],[])
        listaMachine.append(Subservice(index_subservice,row["machine"]))
        dicSubservice.setdefault(row["machine"],index_subservice)
        index_subservice+=1

    print(dicService, dicSubservice)
    index=200
    listService=[]
    for location, listaMachine in dicService.items():
        listService.append(Service(index, "machine_selection", location, [vars(ob) for ob in listaMachine]))
        index+=1
    Service.insertBatch(listService)


    #get users
    users_dic= getUsersDic(getRoles())

    listUser=[]
    for k,v in users_dic.items():
        listUser.append(User(v["id"],k))
    User.insertBatch(listUser)


    #*****InsertInteractions Machine Selections******
    listInteractions=[]
    compoundList=[]
    inter_seq_index=1000
    for i, row in dfList.iterrows():
        lc=[Context(contextDic[row["shift"]], row["shift"]), Context(users_dic[row.user_id]["idrole"], users_dic[row.user_id]["role"])]
        inter = InteractionSequence(str(inter_seq_index), str(getTimestamp(row.start_date)), str(getTimestamp(row.end_date)), str(users_dic[row.user_id]["id"]),
                                    str(dicSubservice[row.machine]), [vars(ob) for ob in lc], str(1))
        individual = Interaction(inter_seq_index , str(inter_seq_index), row.list_sequence[0], 1)
        compoundList.append(individual)
        inter_seq_index+=1
        print(vars(inter))

        listInteractions.append(inter)

    upload_batches(listInteractions, compoundList)

