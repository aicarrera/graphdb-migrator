import Connection.APIconnection as API
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from model.MarkovChainRecommender import MarkovChainRecommender
from model.evaluator import last_session_out_split, eval_seqreveal, f_measure


r=API.query_to_API("getSequenceInteractionsByContextValue",{"value":""})
df=pd.DataFrame.from_dict(r)
print(df)

#Get train and test
train, test = last_session_out_split(df)
print("Train sessions: {} - Test sessions: {}".format(len(train), len(test)))


print("*****MixedMarkovChainRecommender******")
end= 3
listMC=[]
for i in range(1,end+1):
    mmcrecommender = MarkovChainRecommender(i)
    mmcrecommender.fit(train)
    listMC.append(mmcrecommender)

# hide-output
results_metrics={"Metrics":[],"mean":[],"Model":[], "sd":[]}

for model in listMC :
    results = eval_seqreveal(model,test,train)
    dicResults = {
        "Model": type(model).__name__,
        "GIVEN_K": results[1],
        "LOOK_AHEAD": results[2],
        "STEP": results[3],
        "Precision@3": results[0][0][0],
        "Recall@3": results[0][0][1],
        "MRR@3": results[0][0][2],
    }
    m=results[0][1]
    results_metrics["Metrics"].append("Precision")
    results_metrics["Model"].append(model.name)
    results_metrics["mean"].append(m[:,0].mean())
    results_metrics["sd"].append(m[:, 0].std())

    results_metrics["Metrics"].append("Recall")
    results_metrics["Model"].append(model.name)
    results_metrics["mean"].append(m[:, 1].mean())
    results_metrics["sd"].append(m[:, 1].std())

    results_metrics["Metrics"].append("MRR")
    results_metrics["Model"].append(model.name)
    results_metrics["mean"].append(m[:,2].mean())
    results_metrics["sd"].append(m[:, 2].std())

    results_metrics["Metrics"].append("F1")
    results_metrics["Model"].append(model.name)
    results_metrics["mean"].append(f_measure(m[:,0].mean(),m[:,1].mean()))
    results_metrics["sd"].append(0)

    for k, v in dicResults.items():
        print(k, v)

    print("F-MEASURE", f_measure(results[0][0],results[0][1]))

for k, v in results_metrics.items():
    print(k, v)

metrics_df= pd.DataFrame.from_dict(results_metrics)
print(metrics_df)

g=sns.catplot(data=metrics_df, x="Metrics", y="mean", hue="Model", aspect=0.6, kind="bar", height=4, palette=sns.color_palette("deep"))
g.set(ylim=(0, 1))
plt.yticks([0.1, 0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
plt.show()


