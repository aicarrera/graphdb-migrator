import pandas as pd
df_items= pd.read_csv("ga4/items_ontology.csv")
items_dic = df_items.set_index('name')['id'].to_dict()
print(items_dic)
def extract_emotion(event):
    if "happy" in event:
        return "happy"
    elif "sad" in event:
        return "sad"
    elif "meh" in event:
        return "indifferent"
    else:
        return None
def getValueInteraction(event):
    if "btn5no_" in event.lower():
        return -1
def extract_service(event):
   for k in items_dic:
       if k.lower() in event.lower():
           return k

file_names = ['15-03-2023.csv', '16-03-2023.csv']

# Read each file into a separate dataframe
dfs = []
for file in file_names:
    df = pd.read_csv("ga4/"+file)
    dfs.append(df)

users_dic = {}
combined_df = pd.concat(dfs, ignore_index=True)


for i, row in combined_df.iterrows():
    if row.user_id not in users_dic and row.page_location.split("=")[-1].isalpha():
        users_dic[row.user_id]=row.page_location.split("=")[-1].title()

print(users_dic)
combined_df["a_b_test"]=combined_df.user_id.map(users_dic).apply(eval)
combined_df['emotion'] = combined_df['event_name'].apply(extract_emotion)
combined_df['service'] =  combined_df['event_name'].apply(extract_service)


print(combined_df.groupby(["event_date", "a_b_test", "emotion", "service"]).count())







dfFiltered = combined_df[combined_df.event_name.str.startswith("Btn5")]
dfFiltered.loc[dfFiltered.event_name.str.lower().str.startswith("btn5no_"), 'int_value'] = -1


# normalize the ratings using min-max normalization
dfFiltered["int_value"]=(dfFiltered["int_value"]--1) / (1--1)
print(dfFiltered.groupby(["event_date","int_value","event_name"]).count())

