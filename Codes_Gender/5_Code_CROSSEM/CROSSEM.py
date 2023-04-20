import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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

            hypotheses = [author_tweet]
            references = [algo_tweet]
 
            results = bertscore.compute(predictions=hypotheses, references=references, model_type="distilbert-base-uncased")
            count += round(results['f1'][0],3)

    return count / (len(algo_tweet_list) * len(author_tweet_list))

author_df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Gender/0_Gender_30_Data.txt', sep = "\n\n", header=None, engine='python')
author_df.columns = ['content']
print('lengthhhh', len(author_df))

algo_summ_list = ['ClusterRank', 'DSDRNonLin', 'LexRank', 'SummBasic', 'LSA', 'LUHN', 'RNN_RNN', 'BERT', 'GPT2', 'XLNet']
# algo_summ_list = [ 'RNN_RNN']

# for asl in algo_summ_list :

#     binary_count = 0 
#     fractional_count = 0
#     similarity_count = 0

#     print("Algo Summary " + asl)

#     algo_df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes/Algorithmic_Summaries_2_New/' + asl + '.txt', sep = "\n\n", header=None, engine='python')
#     algo_df.columns = ['content']
#     algo_data = algo_df['content'].tolist()

#     # print("ALGOOOOOO", algo_data)
#     for i in range(NUM_AUTHORS) :

#         author_data = [author_df['content'].iloc[i]]
#         # print("authorrrrr", author_data)
#         binary_count += CROSSEM_B(algo_data, author_data)
#         fractional_count += CROSSEM_F(algo_data, author_data)
#         similarity_count += CROSSEM_S(algo_data, author_data)
        

#     print("Binary : " , round(binary_count / NUM_AUTHORS, 3))
#     print("Fractional : " , round(fractional_count / NUM_AUTHORS, 3))
#     print("Similarity : " , round(similarity_count / NUM_AUTHORS, 3))
#     print("\n")

for asl in algo_summ_list :

    binary_count = 0 
    fractional_count = 0
    similarity_count = 0

    print("Algo Summary " + asl)

    algo_df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Gender/Data_Algo_Summary_Sentences/' + asl + '.txt', sep = "\n\n", header=None, engine='python')
    algo_df.columns = ['content']
    algo_data = algo_df['content'].tolist()

    # print(algo_data)

    for i in range(NUM_AUTHORS) :

        author_data = author_df['content'].iloc[i].split(". ")

        for j in range(len(author_data)-1) :
            author_data[j] = author_data[j] + "."

        # print(author_data)


        binary_count += CROSSEM_B(algo_data, author_data)
        fractional_count += CROSSEM_F(algo_data, author_data)
        similarity_count += CROSSEM_S(algo_data, author_data)

    print("Binary : " , round(binary_count / NUM_AUTHORS, 3))
    print("Fractional : " , round(fractional_count / NUM_AUTHORS, 3))
    print("Similarity : " , round(similarity_count / NUM_AUTHORS, 3))
    print("\n")