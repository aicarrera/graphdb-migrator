import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (precision_recall_curve,
                              PrecisionRecallDisplay)
precision_metrics=[]
recall_metrics=[]

def get_test_sequences(test_data, given_k):
  # we can run evaluation only over sequences longer than abs(LAST_K)
  test_sequences = test_data.loc[test_data.interactionwu_prep.map(len) > abs(given_k), 'interactionwu_prep'].values
  return test_sequences

def get_test_sequences_and_users(test_data, given_k, train_users):
    # we can run evaluation only over sequences longer than abs(LAST_K)
    mask = test_data["interactions"].map(len) > abs(given_k)
    mask &= test_data["idUser"].isin(train_users)
    test_sequences = test_data.loc[mask, "interactions"].values
    test_users = test_data.loc[mask, "idUser"].values
    test_context=test_data.loc[mask, "idContexttmp"].values
    print("*******context",test_context)
    return test_sequences, test_users,test_context

def last_session_out_split(data):
    """
    Assign the last session of every user to the test set and the remaining ones to the training set
    """
    sequences = data.sort_values(by=["idUser", "startDate"]).groupby("idUser")["id"]
    last_sequence = sequences.last()
    train = data[~data.id.isin(last_sequence.values)].copy()
    test = data[data.id.isin(last_sequence.values)].copy()
    return train, test


def f_measure (precision, recall):
    return 2 * (precision * recall) / (precision + recall)

def precision(ground_truth, prediction):
    """
    Compute Precision metric
    :param ground_truth: the ground truth set or sequence
    :param prediction: the predicted set or sequence
    :return: the value of the metric
    """
    ground_truth = remove_duplicates(ground_truth)
    prediction = remove_duplicates(prediction)
    precision_score = count_a_in_b_unique(prediction, ground_truth) / float(len(prediction))
    assert 0 <= precision_score <= 1
    return precision_score


def recall(ground_truth, prediction):
    """
    Compute Recall metric
    :param ground_truth: the ground truth set or sequence
    :param prediction: the predicted set or sequence
    :return: the value of the metric
    """
    ground_truth = remove_duplicates(ground_truth)
    prediction = remove_duplicates(prediction)
    recall_score = 0 if len(prediction) == 0 else count_a_in_b_unique(prediction, ground_truth) / float( len(ground_truth))
    assert 0 <= recall_score <= 1
    return recall_score


def mrr(ground_truth, prediction):
    """
    Compute Mean Reciprocal Rank metric. Reciprocal Rank is set 0 if no predicted item is in contained the ground truth.
    :param ground_truth: the ground truth set or sequence
    :param prediction: the predicted set or sequence
    :return: the value of the metric
    """
    rr = 0.
    for rank, p in enumerate(prediction):
        if p in ground_truth:
            rr = 1. / (rank + 1)
            break
    return rr


def count_a_in_b_unique(a, b):
    """
    :param a: list of lists
    :param b: list of lists
    :return: number of elements of a in b
    """
    count = 0
    for el in a:
        if el in b:
            count += 1
    return count


def remove_duplicates(l):
    return [list(x) for x in set(tuple(x) for x in l)]


def sequential_evaluation(recommender,
                          test_sequences,
                          evaluation_functions,
                          users=None,
                          given_k=1,
                          look_ahead=1,
                          top_n=10,
                          scroll=True,
                          step=1,
                          contexts=None):
    """
    Runs sequential evaluation of a recommender over a set of test sequences
    :param recommender: the instance of the recommender to test
    :param test_sequences: the set of test sequences
    :param evaluation_functions: list of evaluation metric functions
    :param users: (optional) the list of user ids associated to each test sequence. Required by personalized models like FPMC.
    :param given_k: (optional) the initial size of each user profile, starting from the first interaction in the sequence.
                    If <0, start counting from the end of the sequence. It must be != 0.
    :param look_ahead: (optional) number of subsequent interactions in the sequence to be considered as ground truth.
                    It can be any positive number or 'all' to extend the ground truth until the end of the sequence.
    :param top_n: (optional) size of the recommendation list
    :param scroll: (optional) whether to scroll the ground truth until the end of the sequence.
                If True, expand the user profile and move the ground truth forward of `step` interactions. Recompute and evaluate recommendations every time.
                If False, evaluate recommendations once per sequence without expanding the user profile.
    :param step: (optional) number of interactions that will be added to the user profile at each step of the sequential evaluation.
    :return: the list of the average values for each evaluation metric
    """
    if given_k == 0:
        raise ValueError('given_k must be != 0')
    results=[]
    metrics = np.zeros(len(evaluation_functions))
    for i, test_seq in enumerate(test_sequences):
            if users is not None:
                user = users[i]
            else:
                user = None
            if contexts is not None:
                context = contexts[i]
            else:
                context = None

            print("*Sequence:",test_seq,"*")
            # sp= plt.subplots(len(test_seq), 1, figsize=(7, 5), sharex=True)
            if scroll:
                test_seq = [x["element"]+context for x in test_seq]

                r= sequence_sequential_evaluation(recommender,
                                                          test_seq,
                                                          evaluation_functions,
                                                          user,
                                                          given_k,
                                                          look_ahead,
                                                          top_n,
                                                          step,
                                                          context)
                metrics+=r
                results.append(r)
            else:
                r = evaluate_sequence(recommender,
                                             test_seq,
                                             evaluation_functions,
                                             user,
                                             given_k,
                                             look_ahead,
                                             top_n)
                metrics += r
                results.append(r)
            #print(metrics)
            #sns.despine(bottom=True)
            #plt.setp(sp[0].axes, yticks=[], xticks=[])
            #plt.tight_layout()

            #plt.show()
            print("*************************")
    return metrics / len(test_sequences), np.array(results)


def evaluate_sequence(recommender, seq, evaluation_functions, user, given_k, look_ahead, top_n, context, sp):
    """
    :param recommender: which recommender to use
    :param seq: the user_profile/ context
    :param given_k: last element used as ground truth. NB if <0 it is interpreted as first elements to keep
    :param evaluation_functions: which function to use to evaluate the rec performance
    :param look_ahead: number of elements in ground truth to consider. if look_ahead = 'all' then all the ground_truth sequence is considered
    :return: performance of recommender
    """
    # safety checks

    if given_k < 0:
        given_k = len(seq) + given_k

    user_profile = seq[:given_k]
    print("User profile", user_profile)

    ground_truth = seq[given_k:]
    # restrict ground truth to look_ahead
    ground_truth = ground_truth[:look_ahead] if look_ahead != 'all' else ground_truth
    ground_truth = list(map(lambda x: [x], ground_truth))  # list of list format
    print("Ground truth", ground_truth)

    if not user_profile or not ground_truth:
        # if any of the two missing all evaluation functions are 0
        return np.zeros(len(evaluation_functions))

    r = recommender.recommend(user_profile,context, user)[:top_n]
    print("prediction", r, top_n)

    if not r:
        # no recommendation found
        return np.zeros(len(evaluation_functions))
    reco_list = recommender.get_recommendation_list(r)

    tmp_results = []
    for f in evaluation_functions:
        tmp_results.append(f(ground_truth, reco_list))

    print(tmp_results)
    print("-----------------------------------")
    #*****Graph*****
    if sp !=0:
        x1=user_profile+["X"]*(len(seq)-len(user_profile))
        x1= [str(i)+"-"+x1[i-1] for i in range(1,len(x1)+1)]
        y1 = [4]* len(user_profile)+[0]*(len(seq)-len(user_profile))
        splot = sns.barplot(x=x1, y=y1, palette="rocket", ax=sp[1][given_k-1])
        splot.bar_label(splot.containers[0],labels=x1,label_type='center',color="white", fontsize=8)

    return np.array(tmp_results)


def sequence_sequential_evaluation(recommender, seq, evaluation_functions, user, given_k, look_ahead, top_n, step, context,sp=0 ):
    if given_k < 0:
        given_k = len(seq) + given_k

    eval_res = 0.0
    eval_cnt = 0
    for gk in range(given_k, len(seq), step):
        eval_res += evaluate_sequence(recommender, seq, evaluation_functions, user, gk, look_ahead, top_n,context, sp)
        eval_cnt += 1
    print("sequence metrics->",eval_res / eval_cnt)
    precision_metrics.append((eval_res / eval_cnt)[0])
    recall_metrics.append((eval_res / eval_cnt)[1])
    return eval_res / eval_cnt

METRICS = {'precision':precision,
           'recall':recall,
           'mrr': mrr}
TOPN=3# length of the recommendation list taking the average of the existing sequences
# collapse
def eval_seqreveal(recommender,test,train, user_flg=0):
    GIVEN_K = 1
    LOOK_AHEAD = 1
    STEP = 1

    if user_flg:
        test_sequences, test_users,test_context = get_test_sequences_and_users(test, GIVEN_K, train.user.values)
        print(
            '{} Sequences available for evaluation ({} users)'.format(len(test_sequences), len(np.unique(test_users))))
        results = sequential_evaluation(recommender,
                                        test_sequences=test_sequences,
                                        users=test_users,
                                        given_k=GIVEN_K,
                                        look_ahead=LOOK_AHEAD,
                                        evaluation_functions=METRICS.values(),
                                        top_n=TOPN,
                                        scroll=True,  # scrolling averages metrics over all profile lengths
                                        step=STEP)
    else:
       # test_sequences = get_test_sequences(test, GIVEN_K)
       test_sequences, test_users, test_context = get_test_sequences_and_users(test, GIVEN_K, train["idUser"].values)
       print('{} sequences available for evaluation'.format(len(test_sequences)))
       results = sequential_evaluation(recommender,
                                        test_sequences=test_sequences,
                                        given_k=GIVEN_K,
                                        look_ahead=LOOK_AHEAD,
                                        evaluation_functions=METRICS.values(),
                                        top_n=TOPN,
                                        scroll=True,  # scrolling averages metrics over all profile lengths
                                        step=STEP,
                                        contexts=test_context)

    # print('Sequential evaluation (GIVEN_K={}, LOOK_AHEAD={}, STEP={})'.format(GIVEN_K, LOOK_AHEAD, STEP))
    # for mname, mvalue in zip(METRICS.keys(), results):
    #     print('\t{}@{}: {:.4f}'.format(mname, TOPN, mvalue))

    return [results, GIVEN_K, LOOK_AHEAD, STEP]

