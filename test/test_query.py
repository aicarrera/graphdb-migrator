import Connection.APIconnection as API
import pandas as pd

r=API.query_to_API("getSequenceInteractionsByContextValue",{"value":""})
df=pd.DataFrame.from_dict(r)
print(df.head())
print(r)
print(len(r))