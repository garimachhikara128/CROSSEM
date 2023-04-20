from rouge_metric import PyRouge
import pandas as pd
import numpy as np

SAVING = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Data_Metrics_10'
human_summaries = ['R1', 'R2', 'R3', 'L1', 'L2', 'L3']
algo_summaries = ['ClusterRank', 'DSDRNonLin', 'LexRank', 'SummBasic', 'LSA', 'LUHN', 'RNN_RNN']
# metrics = ['rouge-1', 'rouge-2', 'rouge-4', 'rouge-l', 'rouge-w-1.2', 'rouge-s4', 'rouge-su4']
metrics = ['rouge-l']

def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))

for m in metrics : 

    main_list = []
    for algo in algo_summaries :
        
        row_list = []
        for human in human_summaries :
            
            algo_summ_file = open('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Data_Algo_Summary_10/' + algo + '.txt', 'r')
            algo_summ = algo_summ_file.read()
            human_summ_file = open('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Data_Human_Summary/' + human + '.txt', 'r')
            human_summ = human_summ_file.read()

            hypotheses = [
                algo_summ
            ]
            references = [[
                human_summ
            ]]

            # print(algo , human)
            rouge = PyRouge(rouge_n=(1, 2, 4), rouge_l=True, rouge_w=True, rouge_w_weight=1.2, rouge_s=True, rouge_su=True, skip_gap=4)
            scores = rouge.evaluate(hypotheses, references)

            row_list.append(round(scores[m]['f'],3))

        # main_list.append(row_list)
        print(algo)
        print(round(gini(np.array(row_list)),3))
        print("\n")
    
    # df = pd.DataFrame(main_list, columns=human_summaries) 
    # df.to_csv(SAVING + '/' + m + '.csv', index=True) 