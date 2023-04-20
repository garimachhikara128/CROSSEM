import pandas as pd
import numpy as np
 
def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))

df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Data_Author_Scores/Vaccine.csv')
df = df.reset_index()

# print(df.columns)

l = ['Cluster Rank', 'DSDR Non Linear',	'Lex Rank',	'Summ Basic', 'LSA', 'LUHN', 'Summa RNN-RNN']

print('\nPoint 1 : How much satisfied with each summary :-\n')

for i in range (7) :

    summary_column = df['How much are you satisfied with the ' + l[i] + ' summary ?']
    affiliation_column = df['Please describe your attitudes towards the COVID-19 (Coronavirus) vaccines.']

    forsum = 0 
    againstsum = 0 
    allsum = 0
    forcount = 0
    againstcount = 0 
    allcount = 0 

    all_list = []

    for affiliation, summary in zip(affiliation_column, summary_column) :

        allcount += 1
        allsum += summary 
        all_list.append(summary)

        if affiliation == 'For (I feel positively about the vaccines)' :
            forsum += summary 
            forcount += 1

        elif affiliation == 'Against (I feel negatively about the vaccines)' :
            againstsum += summary 
            againstcount += 1

    
    print('Results for ' , l[i], ' :- ')
    # print('All Avg' , round(allsum / allcount, 3))  
    # print('For Avg' , round(forsum / forcount, 3))  
    # print('Against Avg' , round(againstsum / againstcount, 3))
    print(round(gini(np.array(all_list)),3))
    print('\n')
