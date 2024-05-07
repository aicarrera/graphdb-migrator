import pandas as pd
import sys
import urllib.request
from urllib.error import HTTPError

df=pd.read_csv("papers.csv",delimiter=";")
df["process"]=df.process.str.replace("\n"," ")
df["runtime"]=df.runtime.str.replace("\n"," ")
df["cite"] = ""


BASE_URL = 'http://dx.doi.org/'
file_TXT = open("bibtex.txt", "w")

for i , row in df.iterrows():
    print(row.doi, row.title)
    if pd.isna(row.doi):
        continue
    url = BASE_URL + row.doi.strip()
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/x-bibtex')
    try:
        with urllib.request.urlopen(req) as f:
            bibtex = f.read().decode()
            row.cite=bibtex.split(",")[0].split("{")[-1]
            file_TXT.write(bibtex+"\n")
    except HTTPError as e:
        if e.code == 404:
            print('DOI not found.')
        else:
            print('Service unavailable.')
file_TXT.close()

print("*****************", df["cite"])
a=open("parameters.csv","w")
process_dict={}
runtime_dict={}
for i , row in df.iterrows():

    if not pd.isna(row.process):
        process_list= row.process.lower().split(";")
        process_list= [x.strip() for x in process_list]
        process_list = [x.rstrip("s") for x in process_list]

        for x in process_list:
           l=process_dict.setdefault(x,[])
           l.append(row.cite)

    if not pd.isna(row.runtime):
        runtime_list = row.runtime.lower().split(";")
        runtime_list = [x.strip() for x in runtime_list]
        for x in runtime_list:
            l = runtime_dict.setdefault(x, [])
            l.append(row.cite)

for k in sorted(process_dict):
    print("{} &\n&\n&\n& {}\n  \\\\\n".format(k,"\\cite{"+",".join(process_dict[k])+"}"))
    a.write("{};{};;{}\n".format(k,"P","\\cite{"+",".join(process_dict[k])+"}"))
for k in sorted(runtime_dict):
    print("{} &\n&\n&\n& {}\n \\\\\n".format( k, "\\cite{"+",".join(runtime_dict[k])+"}"))
    a.write("{};{};;{}\n".format(k,"r","\\cite{"+",".join(runtime_dict[k])+"}"))


a.close()