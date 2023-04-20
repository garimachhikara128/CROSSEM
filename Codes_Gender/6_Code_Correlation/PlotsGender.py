import pandas as pd
 
df = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes/Codes_Plots')
df = df.reset_index()

# print(df.columns)

l = ['Summary 1 (Male)', 'Summary 2 (Male)', 'Summary 3 (Female)', 'Summary 4 (Male)', 'Summary 5 (Female)', 'Summary 6 (Female)']

print('\nPoint 1 : How much satisfied with each summary :-\n')

for i in range (6) :

    summary_column = df['S-' + l[i]]
    gender_column = df['Gender']

    malesum = 0 
    femalesum = 0 
    malecount = 0
    femalecount = 0 

    for gender, summary in zip(gender_column, summary_column) :

        if gender == 'Male' :
            malesum += summary 
            malecount += 1

        elif gender == 'Female' :
            femalesum += summary 
            femalecount += 1

    
    print('Results for ' , l[i], ' :- ')
    print('Male Avg' , round(malesum / malecount, 2))  
    print('Female Avg' , round(femalesum / femalecount, 2))  
    print('\n')

print('\nPoint 3 : Leaning of each summary :-\n')

for i in range (6) :

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

