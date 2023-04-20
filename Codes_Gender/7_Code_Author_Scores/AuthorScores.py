import pandas as pd
 
df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Gender/Data_Raw/AuthorResponses.csv')
df = df.reset_index()

# print(df.columns)

l = ['Cluster Rank', 'DSDR Non Linear',	'Lex Rank',	'Summ Basic', 'LSA', 'LUHN', 'Summa RNN-RNN']

print('\nPoint 1 : How much satisfied with each summary :-\n')

for i in range (7) :

    summary_column = df['S-' + l[i]]
    gender_column = df['Gender']

    malesum = 0 
    femalesum = 0 
    allsum = 0
    malecount = 0
    femalecount = 0 
    allcount = 0 

    for gender, summary in zip(gender_column, summary_column) :

        allcount += 1
        allsum += summary 

        if gender == 'Male' :
            malesum += summary 
            malecount += 1

        elif gender == 'Female' :
            femalesum += summary 
            femalecount += 1

    
    print('Results for ' , l[i], ' :- ')
    print('All Avg' , round(allsum / allcount, 2))  
    print('Female Avg' , round(femalesum / femalecount, 2))  
    print('Male Avg' , round(malesum / malecount, 2))    
    print('\n')

print('\nPoint 2 : Which summary will make you satisfied ?\n')

count_total = 0
count_myopinion = 0
count_my_and_other_opinion = 0
count_doesnt_reflect_my_opinion = 0
count_informative = 0

all_opinion = df['Which summary would satisfy you OR which summary was provided high scores in previous question ?']

for opinion in all_opinion :

    count_total += 1

    if opinion.__contains__('Summary which reflects your opinion') :
        count_myopinion += 1

    if opinion.__contains__('Summary which reflects your opinion + some other opinion') :
        count_my_and_other_opinion += 1

    if opinion.__contains__('Summary which doesn\'t reflect your opinion') :
        count_doesnt_reflect_my_opinion += 1

    if opinion.__contains__('Summary which is informative, will help the reader to understand the issue well') :
        count_informative += 1

print('Summary which reflects your opinion', round(count_myopinion * 100 / count_total, 2))
print('Summary which reflects your opinion + some other opinion', round(count_my_and_other_opinion * 100 / count_total, 2))
print('Summary which doesn\'t reflect your opinion', round(count_doesnt_reflect_my_opinion * 100 / count_total, 2))
print('Summary which is informative, will help the reader to understand the issue well', round(count_informative * 100 / count_total, 2))
print('\n')

print('\nPoint 3 : Leaning of each summary :-\n')

for i in range (7) :

    leaning_column = df['L-' + l[i]]
    gender_column = df['Gender']

    male_maleleaning = 0 
    male_femaleleaning = 0 
    male_balanced = 0 
    malecount = 0

    female_maleleaning = 0 
    female_femaleleaning = 0 
    female_balanced = 0 
    femalecount = 0 

    for gender, leaning in zip(gender_column, leaning_column) :
        
        if gender == 'Male' :

            if leaning.__contains__('Male Leaning') :
                male_maleleaning += 1
            elif leaning.__contains__('Female Leaning') :
                male_femaleleaning += 1
            else :
                male_balanced += 1

            malecount += 1

        elif gender == 'Female' :

            if leaning.__contains__('Male Leaning') :
                female_maleleaning += 1
            elif leaning.__contains__('Female Leaning') :
                female_femaleleaning += 1
            else :
                female_balanced += 1

            femalecount += 1

    print('Results for ' , l[i], ' :- ')

    print("Male Opinion :")
    print('Male Leaning' , round(male_maleleaning * 100 / malecount, 2))  
    print('Female Leaning' , round(male_femaleleaning * 100 / malecount, 2))  
    print('Balanced' , round(male_balanced * 100 / malecount, 2))  
    print('\n')
    print("Female Opinion :")
    print('Male Leaning' , round(female_maleleaning * 100 / femalecount, 2))  
    print('Female Leaning' , round(female_femaleleaning * 100 / femalecount, 2))  
    print('Balanced' , round(female_balanced * 100 / femalecount, 2))  


    print('\n')
