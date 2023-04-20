from evaluate import load
bertscore = load("bertscore")
import numpy as np

def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))

SAVING = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Data_Metrics_10/BertScore.csv'
human_summaries = ['F1', 'F2', 'F3', 'A1', 'A2', 'A3']
algo_summaries = ['ClusterRank', 'DSDRNonLin', 'LexRank', 'SummBasic', 'LSA', 'LUHN', 'RNN_RNN']

main_list = []

for algo in algo_summaries :
        
        row_list = []
        for human in human_summaries :
            
            algo_summ_file = open('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Data_Algo_Summary_10/' + algo + '.txt', 'r')
            algo_summ = algo_summ_file.read()
            human_summ_file = open('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Data_Human_Summary/' + human + '.txt', 'r')
            human_summ = human_summ_file.read()

            hypotheses = [algo_summ]
            references = [human_summ]

            # print(hypotheses, references)

            results = bertscore.compute(predictions=hypotheses, references=references, model_type="distilbert-base-uncased")
            row_list.append(round(results['f1'][0],3))

        # main_list.append(row_list)
        print(algo)
        print(round(gini(np.array(row_list)),3))
        print("\n")

# df = pd.DataFrame(main_list, columns=human_summaries) 
# df.to_csv(SAVING, index=True) 
