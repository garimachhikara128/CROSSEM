import pandas as pd
 
df = pd.read_excel('/Users/garima/Downloads/Questions - Reservation (Responses).xlsx')
df = df.reset_index()

# print(df.columns)

l = ['Summary 1 (General)', 'Summary 2 (Reserved)', 'Summary 3 (General)', 'Summary 4 (Reserved)', 'Summary 5 (Reserved)', 'Summary 6 (General)']

print('\nPoint 1 : How much satisfied with each summary :-\n')

for i in range (6) :

    summary_column = df['S-' + l[i]]
    category_column = df['Category']

    generalsum = 0 
    reservedsum = 0 
    generalcount = 0
    reservedcount = 0 

    for category, summary in zip(category_column, summary_column) :

        if category == 'General' :
            generalsum += summary 
            generalcount += 1

        elif category == 'EWS/OBC/SC/ST' :
            reservedsum += summary 
            reservedcount += 1

    
    print('Results for ' , l[i], ' :- ')
    print('General Avg' , round(generalsum / generalcount, 2)) 
    print('Reserved Avg' , round(reservedsum / reservedcount, 2)) 
    print('\n')

print('\nPoint 3 : Leaning of each summary :-\n')

for i in range (6) :

    leaning_column = df['L-' + l[i]]
    category_column = df['Category']

    general_generalleaning = 0 
    general_reservedleaning = 0 
    general_balanced = 0 
    generalcount = 0

    reserved_generalleaning = 0 
    reserved_reservedleaning = 0 
    reserved_balanced = 0 
    reservedcount = 0

    for category, leaning in zip(category_column, leaning_column) :
        
        if category == 'General' :

            if leaning.__contains__('General Leaning') :
                general_generalleaning += 1
            elif leaning.__contains__('Reserved Leaning') :
                general_reservedleaning += 1
            else :
                general_balanced += 1

            generalcount += 1

        elif category == 'EWS/OBC/SC/ST' :

            if leaning.__contains__('General Leaning') :
                reserved_generalleaning += 1
            elif leaning.__contains__('Female Leaning') :
                reserved_reservedleaning += 1
            else :
                reserved_balanced += 1

            reservedcount += 1

    print('Results for ' , l[i], ' :- ')

    print('General Opinion :')
    print('General Leaning' , round(general_generalleaning * 100 / generalcount, 2)) 
    print('Reserved Leaning' , round(general_reservedleaning * 100 / generalcount, 2)) 
    print('Balanced' , round(general_balanced * 100 / generalcount, 2) )
    print('\n')
    print('Reserved Opinion :')
    print('General Leaning' , round(reserved_generalleaning * 100 / reservedcount, 2)) 
    print('Reserved Leaning' , round(reserved_reservedleaning * 100 / reservedcount, 2)) 
    print('Balanced' , round(reserved_balanced * 100 / reservedcount, 2))  
    print('\n')

