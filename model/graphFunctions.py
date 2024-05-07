import networkx as nx
from pprint import pprint
import matplotlib.pyplot as plt


def add_nodes_to_graph_ngrams(train_data, N):
    model={}
    print(train_data.head())
    context= train_data["idContexttmp"].values
    sequences = train_data["interactions"].values
    print(type(sequences), len(sequences))

    for seq,cont in zip(sequences,context):
        s=[x["element"]+cont for x in seq]
        s=tuple(s)
        model.setdefault(cont,{})

        for Nth in range(1,N+1):
            for i in range(len(s) - Nth):
                ngram = tuple(s[i:i + Nth])  # get a slice of length 2 from current position
                next_item = tuple([s[i + Nth]])  # next item is current index plus two (i.e., right after the slice)
                dicValues=model[cont].setdefault(ngram,{})
                dicValues.setdefault(next_item,0)
                dicValues[next_item]+=1  # append this next item to the list for this ngram

    for c in model:
        for k, d in model[c].items():
            tot=sum(list(d.values()))
            for k,v in d.items():
                d[k]=round((v/tot),4)
    print("model->",model)
    # create graph object
    G = nx.DiGraph()

    # nodes correspond to states
    G.add_nodes_from(list(model.keys()))
    #print(f'Nodes:\n{G.nodes()}\n')

    # for x in model:
    #   print(x)
    #   for d, i in model[x].items():
    #       print(d,i)

    # edges represent transition probabilities
    i=0
    for c in model:
        G.add_nodes_from(list(model[c].keys()))
        for k, v in model[c].items():
            G.add_edge(c,k, transitionProb=i, label=c)
            for kval, vval in v.items():
                G.add_edge(k, kval, transitionProb=vval, label=vval)
        i+=1
    return (model, G)



def show_graph(G):
    pprint(G.edges(data=True))

    pos = nx.spring_layout(G, seed=15)  # positions for all nodes - seed for reproducibility
    colors = range(len(G.nodes))
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=colors, cmap=plt.cm.tab20c)

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=6, font_family="sans-serif" )
    # edge weight labels
    nx.draw_networkx_edges(G, pos, width=0.25, edge_color="tab:blue", alpha=0.5, style="dashed",arrows=True, arrowstyle="-",)
    labels = {(n1, n2): d['transitionProb'] for n1, n2, d in G.edges(data=True)}

    edge_labels = nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G,seed=15), edge_labels=labels, font_size=5)

    ax = plt.gca()
    ax.margins(0.02)

    plt.tight_layout()
    plt.show()



