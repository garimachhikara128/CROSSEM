import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
from evaluate import load
bertscore = load("bertscore")

NUM_AUTHORS = 30

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

def CROSSEM_BERT(algo_tweet_list, author_tweet_list) :

    count = 0
    for author_tweet in author_tweet_list :
        for algo_tweet in algo_tweet_list : 

            hypotheses = [author_tweet]
            references = [algo_tweet]
 
            results = bertscore.compute(predictions=hypotheses, references=references, model_type="distilbert-base-uncased")
            count += round(results['f1'][0],3)

    return count / (len(algo_tweet_list) * len(author_tweet_list))

author_df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Original_30_Brexit_Clean.csv', engine='python')
print(author_df.columns)

print('length : ', len(author_df))

algo_summ_list = ['ClusterRank', 'DSDRNonLin', 'LexRank', 'SummBasic', 'LSA', 'LUHN', 'RNN_RNN', 'BERT', 'GPT2', 'XLNet']


for asl in algo_summ_list :

    binary_count = 0 
    fractional_count = 0
    similarity_count = 0
    bert_count = 0

    print("Algo Summary " + asl)

    algo_df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Data_Algo_Summary_10/' + asl + '.txt', sep = "\n\n", header=None, engine='python')
    algo_df.columns = ['content']
    algo_data = algo_df['content'].tolist()

    for i in range(NUM_AUTHORS) :

        author_data = author_df['opinion'].iloc[i]
        author_data = ast.literal_eval(author_data)

        binary_count += CROSSEM_B(algo_data, author_data)
        fractional_count += CROSSEM_F(algo_data, author_data)
        similarity_count += CROSSEM_S(algo_data, author_data)
        # bert_count += CROSSEM_BERT(algo_data, author_data)
        

    print("Binary : " , round(binary_count / NUM_AUTHORS, 3))
    print("Fractional : " , round(fractional_count / NUM_AUTHORS, 3))
    print("Similarity : " , round(similarity_count / NUM_AUTHORS, 3))
    # print("Similarity : " , round(bert_count / NUM_AUTHORS, 3))
    print("\n")
