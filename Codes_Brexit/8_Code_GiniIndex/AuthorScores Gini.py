import pandas as pd
import numpy as np

def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))

df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Data_Author_Scores/Brexit.csv')
df = df.reset_index()

# print(df.columns)

l = ['Cluster Rank', 'DSDR Non Linear',	'Lex Rank',	'Summ Basic', 'LSA', 'LUHN', 'Summa RNN-RNN']

print('\nPoint 1 : How much satisfied with each summary :-\n')

for i in range (7) :

    summary_column = df['How much are you satisfied with the ' + l[i] + ' summary ?']
    affiliation_column = df['In the referendum on whether the UK should remain a member of the EU (BREXIT), how did you vote? (June 23 2016)']

    remainsum = 0 
    leavesum = 0 
    allsum = 0
    remaincount = 0
    leavecount = 0 
    allcount = 0 

    all_list = []

    for affiliation, summary in zip(affiliation_column, summary_column) :

        allcount += 1
        allsum += summary 
        all_list.append(summary)

        if affiliation == 'Remain' :
            remainsum += summary 
            remaincount += 1

        elif affiliation == 'Leave' :
            leavesum += summary 
            leavecount += 1

    
    print('Results for ' , l[i], ' :- ')
    # print('All Avg' , round(allsum / allcount, 3))  
    # print('remain Avg' , round(remainsum / remaincount, 3))  
    # print('leave Avg' , round(leavesum / leavecount, 3))    
    print(round(gini(np.array(all_list)),3))
    print('\n')
    