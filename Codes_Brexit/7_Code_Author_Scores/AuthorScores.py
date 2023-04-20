import pandas as pd
 
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

    for affiliation, summary in zip(affiliation_column, summary_column) :

        allcount += 1
        allsum += summary 

        if affiliation == 'Remain' :
            remainsum += summary 
            remaincount += 1

        elif affiliation == 'Leave' :
            leavesum += summary 
            leavecount += 1

    
    print('Results for ' , l[i], ' :- ')
    print('All Avg' , round(allsum / allcount, 3))  
    print('remain Avg' , round(remainsum / remaincount, 3))  
    print('leave Avg' , round(leavesum / leavecount, 3))    
    print('\n')

print('\nPoint 2 : Which summary will make you satisfied ?\n')

count_total = 0
count_myopinion = 0
count_my_and_other_opinion = 0
count_doesnt_reflect_my_opinion = 0
count_other = 0

all_opinion = df['On topics similar to this, what do you think will constitute a good summary ?']

for opinion in all_opinion :

    count_total += 1

    if opinion == 'Summary which reflects your opinion' :
        count_myopinion += 1

    elif opinion == 'Summary which reflects your opinion + other people\'s opinion' :
        count_my_and_other_opinion += 1

    elif opinion == 'Summary which does not reflect your opinion' :
        count_doesnt_reflect_my_opinion += 1

    else :
        count_other += 1

print('Summary which reflects your opinion', round(count_myopinion * 100 / count_total, 2))
print('Summary which reflects your opinion + other people\'s opinion', round(count_my_and_other_opinion * 100 / count_total, 2))
print('Summary which does not reflect your opinion', round(count_doesnt_reflect_my_opinion * 100 / count_total, 2))
print('Others', round(count_other * 100 / count_total, 2))
print('\n')


print('\nPoint 3 : Leaning of each summary :-\n')

for i in range (7) :

    leaning_column = df['Your opinion about the ' + l[i] + ' summary ?']
    affiliation_column = df['In the referendum on whether the UK should remain a member of the EU (BREXIT), how did you vote? (June 23 2016)']

    remain_remainleaning = 0 
    remain_leaveleaning = 0 
    remain_balanced = 0 
    remaincount = 0

    leave_remainleaning = 0 
    leave_leaveleaning = 0 
    leave_balanced = 0 
    leavecount = 0 

    for affiliation, leaning in zip(affiliation_column, leaning_column) :
        
        if affiliation == 'Remain' :

            if leaning == 'Covers cons of BREXIT' :
                remain_remainleaning += 1
            elif leaning == 'Covers pros of BREXIT' :
                remain_leaveleaning += 1
            else :
                remain_balanced += 1

            remaincount += 1

        elif affiliation == 'Leave' :

            if leaning == 'Covers cons of BREXIT' :
                leave_remainleaning += 1
            elif leaning == 'Covers pros of BREXIT' :
                leave_leaveleaning += 1
            else :
                leave_balanced += 1

            leavecount += 1

    print('Results for ' , l[i], ' :- ')

    print("Remain Opinion :")
    print('Remain Leaning' , round(remain_remainleaning * 100 / remaincount, 3))  
    print('Leave Leaning' , round(remain_leaveleaning * 100 / remaincount, 3))  
    print('Balanced' , round(remain_balanced * 100 / remaincount, 3))  
    print('\n')
    print("Leave Opinion :")
    print('Remain Leaning' , round(leave_remainleaning * 100 / leavecount, 3))  
    print('Leave Leaning' , round(leave_leaveleaning * 100 / leavecount, 3))  
    print('Balanced' , round(leave_balanced * 100 / leavecount, 3))  

    print('\n')
