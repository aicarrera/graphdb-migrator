import logging
from model.graphFunctions import *
from model.ISequentialRecommender import ISequentialRecommender


class MarkovChainRecommender(ISequentialRecommender):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def __init__(self, order):
        """
        :param order: the order of the Markov Chain
        """
        super(MarkovChainRecommender, self).__init__()
        self.order = order
        self.name = "MC order {}".format(self.order)

    def fit(self, train_data):
        logging.info('Building Markov Chain model ' + str(self.order))
        logging.info('Adding nodes')
        self.count_dict, self.G = add_nodes_to_graph_ngrams(train_data, self.order)
        if self.order==1:
            show_graph(self.G)

    def create_subgraph(self, node):
        edges = nx.dfs_successors(self.G, node)
        nodes = []
        for k, v in edges.items():
            nodes.extend([k])
            nodes.extend(v)
        return self.G.subgraph(nodes)

    def recommend(self, user_profile, context=None,user_id=None):
        # if the user profile is longer than the markov order, chop it keeping recent history
        state = tuple(user_profile[-self.order:])
        # see if graph has that state
        recommendations = []
        last = state  # tuple([state[-1]])
        if self.G.has_node(context):
            self.subG = self.create_subgraph(context)
            # search for recommendations in the forward star
            rec_dict = {}
            for u, v in self.subG.edges([last]):
                lastElement = tuple(v[-1:])
                rec_dict[lastElement] = self.subG[u][v]['transitionProb']  # *prob
            for k, v in rec_dict.items():
                recommendations.append((list(k), v))

        rec_dict = {}
        recommendations2 = []
        for i in recommendations:
            rec_dict.setdefault(tuple(i[0]), 0)
            rec_dict[tuple(i[0])] += i[1]

        for k, v in dict(sorted(rec_dict.items(), key=lambda item: item[1], reverse=True)).items():
            recommendations2.append((list(k), v))

        return recommendations2

    def _set_graph_debug(self, G):
        self.G = G
