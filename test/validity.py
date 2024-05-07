import json
import requests

# Loading the credentials headers from config.json
credentials_headers = json.load(open("config.json", "r"))
tests=["class_overlap","class_parity","correlation_detection"]#"data_completeness","data_duplicates","data_homogeneity","data_profiler","feature_relevance","label_purity","outlier_detection"]
jobids=[]
responses=[]
for t in tests:
    with open('sequences_df_prep_simulated_EN.csv', 'r') as fp:
        response = requests.post(
            'https://api.ibm.com/dataquality4ai/run/data_quality/structured/{}'.format(t),
            headers=credentials_headers,
            files={'data_file': fp}
        )
        r=response.json()
        print("Response JSON -", r)
        jobids.append(r["job_id"])
        #print("\nResponse headers -", response.headers)
        # Loading the credentials headers from config.json
        credentials_headers = json.load(open("config.json", "r"))

        response = requests.post(
        'https://api.ibm.com/dataquality4ai/run/get_result',
        headers=credentials_headers,
        data={"job_id": r["job_id"]}
        )

        responses.append(response.json())
print(responses)
for r in responses:
    resp=r["response"]
    print(resp)
    #print("{}-{}".format(resp["name"],resp["type"]))
    #print("score:{}".format(resp["results"]["score"]))
    #print("details:{}".format(resp["results"]["details"]))
    #print("explanation:{}".format(resp["results"]["explanation"]))
    print("*****************************************************\n")