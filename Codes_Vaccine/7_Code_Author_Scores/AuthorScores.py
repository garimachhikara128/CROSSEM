import pandas as pd
 
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

    for affiliation, summary in zip(affiliation_column, summary_column) :

        allcount += 1
        allsum += summary 

        if affiliation == 'For (I feel positively about the vaccines)' :
            forsum += summary 
            forcount += 1

        elif affiliation == 'Against (I feel negatively about the vaccines)' :
            againstsum += summary 
            againstcount += 1

    
    print('Results for ' , l[i], ' :- ')
    print('All Avg' , round(allsum / allcount, 3))  
    print('For Avg' , round(forsum / forcount, 3))  
    print('Against Avg' , round(againstsum / againstcount, 3))    
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
    affiliation_column = df['Please describe your attitudes towards the COVID-19 (Coronavirus) vaccines.']

    for_forleaning = 0 
    for_againstleaning = 0 
    for_balanced = 0 
    forcount = 0

    against_forleaning = 0 
    against_againstleaning = 0 
    against_balanced = 0 
    againstcount = 0 

    for affiliation, leaning in zip(affiliation_column, leaning_column) :
        
        if affiliation == 'For (I feel positively about the vaccines)' :

            if leaning == 'Favours mandatory covid vaccine' :
                for_forleaning += 1
            elif leaning == 'Against mandatory covid vaccine' :
                for_againstleaning += 1
            else :
                for_balanced += 1

            forcount += 1

        elif affiliation == 'Against (I feel negatively about the vaccines)' :

            if leaning == 'Favours mandatory covid vaccine' :
                against_forleaning += 1
            elif leaning == 'Against mandatory covid vaccine' :
                against_againstleaning += 1
            else :
                against_balanced += 1

            againstcount += 1

    print('Results for ' , l[i], ' :- ')

    print("For Opinion :")
    print('For Leaning' , round(for_forleaning * 100 / forcount, 3))  
    print('Against Leaning' , round(for_againstleaning * 100 / forcount, 3))  
    print('Balanced' , round(for_balanced * 100 / forcount, 3))  
    print('\n')
    print("Against Opinion :")
    print('For Leaning' , round(against_forleaning * 100 / againstcount, 3))  
    print('Against Leaning' , round(against_againstleaning * 100 / againstcount, 3))  
    print('Balanced' , round(against_balanced * 100 / againstcount, 3))  

    print('\n')
