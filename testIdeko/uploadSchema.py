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
dSignals= {1:{
    "_id": "WKC_SKB3Z2",
    "client": "IDEKO",
    "data": {
        "data-schemas": [
            {
                "alias": "TDOMONWH2X1",
                "name": "TDOMONWH2X1",
                "regex": "TDOMONWH2X1",
                "values": {
                    "f1": {
                        "human-name": "Wheelhead2Power",
                        "unit": "W"
                    },
                    "f10": {
                        "human-name": "CAxisSpeed_actual",
                        "unit": "rpm"
                    },
                    "f2": {
                        "human-name": "Wheelhead2Speed_actual",
                        "unit": "mm/min"
                    },
                    "f3": {
                        "human-name": "X1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "X1AxisSpeed_commanded",
                        "unit": "mm/min"
                    },
                    "f5": {
                        "human-name": "X1AxisSpeed_actual",
                        "unit": "mm/min"
                    },
                    "f6": {
                        "human-name": "X1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f7": {
                        "human-name": "X1AxisPosition_commanded",
                        "unit": "mm"
                    },
                    "f8": {
                        "human-name": "CAxisTorque",
                        "unit": "N*m"
                    },
                    "f9": {
                        "human-name": "CAxisSpeed_commanded",
                        "unit": "rpm"
                    }
                }
            },
            {
                "alias": "TDOMONWH1X1",
                "name": "TDOMONWH1X1",
                "regex": "TDOMONWH1X1",
                "values": {
                    "f1": {
                        "human-name": "Wheelhead1Power",
                        "unit": "W"
                    },
                    "f10": {
                        "human-name": "CAxisSpeed_actual",
                        "unit": "rpm"
                    },
                    "f2": {
                        "human-name": "Wheelhead1Speed_actual",
                        "unit": "mm/min"
                    },
                    "f3": {
                        "human-name": "X1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "X1AxisSpeed_commanded",
                        "unit": "mm/min"
                    },
                    "f5": {
                        "human-name": "X1AxisSpeed_actual",
                        "unit": "mm/min"
                    },
                    "f6": {
                        "human-name": "X1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f7": {
                        "human-name": "X1AxisPosition_commanded",
                        "unit": "mm"
                    },
                    "f8": {
                        "human-name": "CAxisTorque",
                        "unit": "N*m"
                    },
                    "f9": {
                        "human-name": "CAxisSpeed_commanded",
                        "unit": "rpm"
                    }
                }
            },
            {
                "alias": "TDOMONWH2X1Z1",
                "name": "TDOMONWH2X1Z1",
                "regex": "TDOMONWH2X1Z1",
                "values": {
                    "f1": {
                        "human-name": "Wheelhead2Power",
                        "unit": "W"
                    },
                    "f10": {
                        "human-name": "Wheelhead2Speed_actual",
                        "unit": "rpm"
                    },
                    "f2": {
                        "human-name": "X1AxisForce",
                        "unit": "N"
                    },
                    "f3": {
                        "human-name": "Z1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "CAxisPower",
                        "unit": "W"
                    },
                    "f5": {
                        "human-name": "CAxisTorque",
                        "unit": "N*m"
                    },
                    "f6": {
                        "human-name": "CAxisSpeed_actual",
                        "unit": "rpm"
                    },
                    "f7": {
                        "human-name": "Z1AxisSpeed_commanded",
                        "unit": "mm/min"
                    },
                    "f8": {
                        "human-name": "X1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f9": {
                        "human-name": "X1AxisSpeed_actual",
                        "unit": "mm/min"
                    }
                }
            },
            {
                "alias": "TDOMONWH1X1Z1",
                "name": "TDOMONWH1X1Z1",
                "regex": "TDOMONWH1X1Z1",
                "values": {
                    "f1": {
                        "human-name": "Wheelhead1Power",
                        "unit": "W"
                    },
                    "f10": {
                        "human-name": "Wheelhead2Speed_actual",
                        "unit": "rpm"
                    },
                    "f2": {
                        "human-name": "X1AxisForce",
                        "unit": "N"
                    },
                    "f3": {
                        "human-name": "Z1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "CAxisPower",
                        "unit": "W"
                    },
                    "f5": {
                        "human-name": "CAxisTorque",
                        "unit": "N*m"
                    },
                    "f6": {
                        "human-name": "CAxisSpeed_actual",
                        "unit": "rpm"
                    },
                    "f7": {
                        "human-name": "Z1AxisSpeed_commanded",
                        "unit": "mm/min"
                    },
                    "f8": {
                        "human-name": "X1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f9": {
                        "human-name": "X1AxisSpeed_actual",
                        "unit": "mm/min"
                    }
                }
            },
            {
                "alias": "TDOMONWH2Z1",
                "name": "TDOMONWH2Z1",
                "regex": "TDOMONWH2Z1",
                "values": {
                    "f1": {
                        "human-name": "Wheelhead2Power",
                        "unit": "W"
                    },
                    "f10": {
                        "human-name": "CAxisSpeed_actual",
                        "unit": "rpm"
                    },
                    "f2": {
                        "human-name": "Wheelhead2Speed_actual",
                        "unit": "N"
                    },
                    "f3": {
                        "human-name": "Z1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "Z1AxisSpeed_commanded",
                        "unit": "mm/min"
                    },
                    "f5": {
                        "human-name": "Z1AxisSpeed_actual",
                        "unit": "mm/min"
                    },
                    "f6": {
                        "human-name": "Z1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f7": {
                        "human-name": "Z1AxisSpeed_commanded",
                        "unit": "mm/min"
                    },
                    "f8": {
                        "human-name": "CAxisTorque",
                        "unit": "N*m"
                    },
                    "f9": {
                        "human-name": "CAxisSpeed_commanded",
                        "unit": "mm/min"
                    }
                }
            },
            {
                "alias": "TDOMONWH1Z1",
                "name": "TDOMONWH1Z1",
                "regex": "TDOMONWH1Z1",
                "values": {
                    "f1": {
                        "human-name": "Wheelhead1Power",
                        "unit": "W"
                    },
                    "f10": {
                        "human-name": "CAxisSpeed_actual",
                        "unit": "rpm"
                    },
                    "f2": {
                        "human-name": "Wheelhead1Speed_actual",
                        "unit": "N"
                    },
                    "f3": {
                        "human-name": "Z1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "Z1AxisSpeed_commanded",
                        "unit": "mm/min"
                    },
                    "f5": {
                        "human-name": "Z1AxisSpeed_actual",
                        "unit": "mm/min"
                    },
                    "f6": {
                        "human-name": "Z1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f7": {
                        "human-name": "Z1AxisSpeed_commanded",
                        "unit": "mm/min"
                    },
                    "f8": {
                        "human-name": "CAxisTorque",
                        "unit": "N*m"
                    },
                    "f9": {
                        "human-name": "CAxisSpeed_commanded",
                        "unit": "mm/min"
                    }
                }
            },
            {
                "alias": "Micra a micra Eje X",
                "name": "010020",
                "regex": "010020",
                "values": {
                    "f1": {
                        "human-name": "X1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "X1AxisEncoder",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "X1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "X1AxisPosition_commanded",
                        "unit": "mm"
                    }
                }
            },
            {
                "alias": "Micra a micra Eje Z",
                "name": "020020",
                "regex": "020020",
                "values": {
                    "f1": {
                        "human-name": "Z1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "Z1AxisEncoder",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "Z1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "Z1AxisPosition_commanded",
                        "unit": "mm"
                    }
                }
            },
            {
                "alias": "Circularidad CCW Eje X y Z",
                "name": "012011",
                "regex": "012011",
                "values": {
                    "f1": {
                        "human-name": "X1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "X1AxisEncoder",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "X1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "Z1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f5": {
                        "human-name": "Z11AxisEncoder",
                        "unit": "mm"
                    },
                    "f6": {
                        "human-name": "Z1AxisForce",
                        "unit": "N"
                    }
                }
            },
            {
                "alias": "Circularidad Eje X y Z",
                "name": "012010",
                "regex": "012010",
                "values": {
                    "f1": {
                        "human-name": "X1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "X1AxisEncoder",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "X1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "Z1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f5": {
                        "human-name": "Z11AxisEncoder",
                        "unit": "mm"
                    },
                    "f6": {
                        "human-name": "Z1AxisForce",
                        "unit": "N"
                    }
                }
            }
        ]
    },
    "machine-id": "WKC_SKB3Z2",
    "machine-name": "LG600B6-100636-IDK",
    "model": "lg",
    "company": "danobat"
},

2:{
    "_id": "XZC_7T1J8A",
    "client": "IDEKO",
    "data": {
        "data-schemas": [
            {
                "alias": "Micra a micra Eje X",
                "name": "010020",
                "regex": "010020",
                "values": {
                    "f1": {
                        "human-name": "XAxisPosition_rotary",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "XAxisPosition_linear",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "XAxis_Force",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "XAxisPosition_commanded",
                        "unit": "mm"
                    }
                }
            },
            {
                "alias": "Micra a micra Eje Y",
                "name": "020020",
                "regex": "020020",
                "values": {
                    "f1": {
                        "human-name": "YAxisPosition_rotary",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "YAxisPosition_linear",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "YAxis_Force",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "YAxisPosition_commanded",
                        "unit": "mm"
                    }
                }
            },
            {
                "alias": "Circularidad CCW Eje X y Y",
                "name": "012011",
                "regex": "012011",
                "values": {
                    "f1": {
                        "human-name": "XAxisPosition_rotary",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "YAxisPosition_rotary",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "XAxisPosition_linear",
                        "unit": "mm"
                    },
                    "f4": {
                        "human-name": "YAxisPosition_linear",
                        "unit": "mm"
                    },
                    "f5": {
                        "human-name": "XAxis_Force",
                        "unit": "N"
                    },
                    "f6": {
                        "human-name": "XAxisPosition_commanded",
                        "unit": "mm"
                    },
                    "f7": {
                        "human-name": "YAxis_Force",
                        "unit": "N"
                    },
                    "f8": {
                        "human-name": "YAxisPosition_commanded",
                        "unit": "mm"
                    }
                }
            },
            {
                "alias": "Circularidad Eje X y Y",
                "name": "012010",
                "regex": "012010",
                "values": {
                    "f1": {
                        "human-name": "XAxisPosition_rotary",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "YAxisPosition_rotary",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "XAxisPosition_linear",
                        "unit": "mm"
                    },
                    "f4": {
                        "human-name": "YAxisPosition_linear",
                        "unit": "mm"
                    },
                    "f5": {
                        "human-name": "XAxis_Force",
                        "unit": "N"
                    },
                    "f6": {
                        "human-name": "XAxisPosition_commanded",
                        "unit": "mm"
                    },
                    "f7": {
                        "human-name": "YAxis_Force",
                        "unit": "N"
                    },
                    "f8": {
                        "human-name": "YAxisPosition_commanded",
                        "unit": "mm"
                    }
                }
            },
            {
                "alias": "Vaiven Eje X",
                "name": "010030",
                "regex": "010030",
                "values": {
                    "f1": {
                        "human-name": "XAxisPosition_rotary",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "XAxisPosition_linear",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "XAxis_Force",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "XAxisPosition_commanded",
                        "unit": "mm"
                    }
                }
            },
            {
                "alias": "Vaiven Eje Y",
                "name": "020030",
                "regex": "020030",
                "values": {
                    "f1": {
                        "human-name": "YAxisPosition_rotary",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "YAxisPosition_linear",
                        "unit": "mm"
                    },
                    "f3": {
                        "human-name": "YAxis_Force",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "YAxisPosition_commanded",
                        "unit": "mm"
                    }
                }
            }
        ],
        "events": {
            "categories": [
                {
                    "color": "#ed110d",
                    "name": "diamantado"
                }
            ],
            "values": []
        }
    },
    "machine-id": "XZC_7T1J8A",
    "machine-name": "BANCO ENSAYOS",
    "segment": "IDEKO",
    "model": "lg",
    "company": "danobat"
},
3:{
    "_id": "CXN_JW7QYA",
    "client": "IDEKO",
    "data": {
        "data-schemas": [
            {
                "alias": "TDOMONWH2X1Z1",
                "name": "TDOMONWH2X1Z1",
                "regex": "TDOMONWH2X1Z1",
                "values": {
                    "f1": {
                        "human-name": "Wheelhead2Power",
                        "unit": "W"
                    },
                    "f10": {
                        "human-name": "X1AxisPosition_actual",
                        "unit": "mm"
                    },
                    "f2": {
                        "human-name": "Wheelhead2Speed_actual",
                        "unit": "mm/min"
                    },
                    "f3": {
                        "human-name": "X1AxisForce",
                        "unit": "N"
                    },
                    "f4": {
                        "human-name": "Z1AxisForce",
                        "unit": "N"
                    },
                    "f5": {
                        "human-name": "CAxisPower",
                        "unit": "W"
                    },
                    "f6": {
                        "human-name": "CAxisTorque",
                        "unit": "N*m"
                    },
                    "f7": {
                        "human-name": "CAxisSpeed_actual",
                        "unit": "rpm"
                    },
                    "f8": {
                        "human-name": "X1AxisSpeed_commanded",
                        "unit": "mm/min"
                    },
                    "f9": {
                        "human-name": "Z1AxisSpeed_commanded",
                        "unit": "mm/min"
                    }
                }
            }
        ]
    },
    "machine-id": "CXN_JW7QYA",
    "machine-name": "110000556 DEC",
    "model": "lg",
    "company": "danobat"
}}


dicService={}
dicSubservice={}
id=500

listaSchema=[]
for k, d in dSignals.items():
    for dicIntern in d["data"]["data-schemas"]:
        listaSchema.append(Subservice(id, dicIntern["alias"].replace(",","-")))
        dicSubservice[dicIntern["alias"]]=id
        id+=1
print(dicSubservice)
listService = []
index=500
listService.append(Service(index, "schema_monitoring", None, [vars(ob) for ob in listaSchema]))
index += 1
Service.insertBatch(listService)






# *****InsertInteractions Machine Selections******

df = pd.read_csv('processedSequences.csv', sep=",")
dfSchema= df[df["event_general"] == "dataSchema_change"]
print(dfSchema[["user_id", "unifiedEvent","event_label","event_general"]].groupby(["user_id", "unifiedEvent","event_label"]).count())

dfList = pd.read_csv('processedSequencesList.csv')

# get users
users_dic = getUsersDic(getRoles())
contextDic = {"t1": 41, "t2": 42}

uploadInter=True
if uploadInter:
    inter_seq_index=5000
    listInteractions=[]
    compoundList=[]
    for i, row in dfSchema.iterrows():
        lc = [Context(contextDic[row["shift"]], row["shift"]),
              Context(users_dic[row.user_id]["idrole"], users_dic[row.user_id]["role"])]
        inter = InteractionSequence(str(inter_seq_index), str(getTimestamp(row.start_date)), str(getTimestamp(row.end_date)),
                                    str(users_dic[row.user_id]["id"]),
                                    str(dicSubservice[row.event_label]), [vars(ob) for ob in lc], str(1))
        individual = Interaction(inter_seq_index, str(inter_seq_index), row.unifiedEvent, 1)
        compoundList.append(individual)
        inter_seq_index += 1
        print(vars(inter))

        listInteractions.append(inter)


    upload_batches(listInteractions,compoundList)

    for i, row in dfList.iterrows():
        lc = [Context(contextDic[row["shift"]], row["shift"]),
              Context(users_dic[row.user_id]["idrole"], users_dic[row.user_id]["role"])]
        inter = InteractionSequence(str(inter_seq_index), str(getTimestamp(row.start_date)),
                                    str(getTimestamp(row.end_date)),
                                    str(users_dic[row.user_id]["id"]),
                                    str(dicSubservice["TDOMONWH2X1"]), [vars(ob) for ob in lc], str(0.5))
        individual = Interaction(inter_seq_index, str(inter_seq_index), "dataSchema_tdomonwh2x1_change", 1)
        compoundList.append(individual)
        inter_seq_index += 1
        print(vars(inter))

        listInteractions.append(inter)

    upload_batches(listInteractions, compoundList)


