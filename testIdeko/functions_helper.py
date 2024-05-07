from datetime import datetime
import pandas as pd
from classes.Interaction_sequence import *
from classes.Interaction import *

roles={ "GeneralResearcher":10, "GrindingResearcher":11,"NDTResearcher":12, "PrecisionResearcher":13}
def getRoles():
    return roles

def getUsersDic(dicRoles):
    # *****Insert Users*****
    df_users = pd.read_csv('users.csv', sep=",")
    users_dic = {}
    for i, row in df_users.iterrows():
        users_dic.setdefault(row["user"], {"id":row["user_id"], "idrole":dicRoles[row["role"]], "role":row["role"]})
    return users_dic

def getTimestamp(date_string):
    date_format = "%Y-%m-%d %H:%M:%S.%f%z"
    print(date_string)
    # Parse the date string into a datetime object
    date_object = datetime.strptime(date_string, date_format)

    # Convert the datetime object to a timestamp (seconds since the epoch)
    timestamp = date_object.timestamp()

    print(timestamp)
    return int(timestamp)

def useTimeLabel(current_hour):
    if 8 <= current_hour <= 13:
        return 't1'
    elif 14 <= current_hour <= 19:
        return 't2'
    else:
        return 't2'


def upload_batches(listInteractions, compoundList):
    # Assuming listInteractions is your list of interactions
    batch_size = 10  # Set the batch size to 20

    # Calculate the total number of batches
    total_batches = len(listInteractions) // batch_size

    # Iterate through the batches
    for batch_index in range(total_batches + 1):
        start = batch_index * batch_size
        end = start + batch_size

        # Extract a batch of interactions
        batch = listInteractions[start:end]

        # Upload the batch
        InteractionSequence.insertBatch(batch)

    Interaction.insertBatch(compoundList)