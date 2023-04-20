import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
import numpy as np

NUM_AUTHORS = 30

def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))

def CROSSEM_B(algo_tweet_list, author_tweet_list) :

    count = 0
    for author_tweet in author_tweet_list :
      
        if author_tweet in algo_tweet_list :
            count += 1

    return 1 if(count >= 1) else 0


def CROSSEM_F(algo_tweet_list, author_tweet_list) :

    count = 0
    for author_tweet in author_tweet_list :
      
        if author_tweet in algo_tweet_list :
            count += 1
    
    return count / len(author_tweet_list)

def CROSSEM_S(algo_tweet_list, author_tweet_list) :

    count = 0
    for author_tweet in author_tweet_list :
        for algo_tweet in algo_tweet_list : 

            data = [author_tweet, algo_tweet] 

            count_vectorizer = CountVectorizer()
            vector_matrix = count_vectorizer.fit_transform(data)

            cosine_similarity_matrix = cosine_similarity(vector_matrix)
            count += cosine_similarity_matrix[0][1]   

    return count / (len(algo_tweet_list) * len(author_tweet_list))

author_df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Original_30_Brexit_Clean.csv', engine='python')
print(author_df.columns)

print('length : ', len(author_df))

algo_summ_list = ['ClusterRank', 'DSDRNonLin', 'LexRank', 'SummBasic', 'LSA', 'LUHN', 'RNN_RNN']

for asl in algo_summ_list :

    binary_count = 0 
    fractional_count = 0
    similarity_count = 0
    bert_count = 0

    print("Algo Summary " + asl)

    algo_df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Data_Algo_Summary_10/' + asl + '.txt', sep = "\n\n", header=None, engine='python')
    algo_df.columns = ['content']
    algo_data = algo_df['content'].tolist()

    sim_list = []

    for i in range(NUM_AUTHORS) :

        author_data = author_df['opinion'].iloc[i]
        author_data = ast.literal_eval(author_data)

        # binary_count += CROSSEM_B(algo_data, author_data)
        # fractional_count += CROSSEM_F(algo_data, author_data)
        similarity_count = CROSSEM_S(algo_data, author_data)
        sim_list.append(similarity_count)
        # bert_count += CROSSEM_BERT(algo_data, author_data)
        

    # print("Binary : " , round(binary_count / NUM_AUTHORS, 3))
    # print("Fractional : " , round(fractional_count / NUM_AUTHORS, 3))
    # print("Similarity : " , round(similarity_count / NUM_AUTHORS, 3))
    # print("Similarity : " , round(bert_count / NUM_AUTHORS, 3))
    print("Gini Index : " , round(gini(np.array(sim_list)),3))
    print("\n")
