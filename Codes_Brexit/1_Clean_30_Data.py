from json.tool import main
from xml.etree.ElementTree import PI
import pandas as pd

PA = 'In the referendum on whether the UK should remain a member of the EU (BREXIT), how did you vote? (June 23 2016)'
PID = 'Please enter your Prolific ID'

data = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Original_30_Brexit.csv')
SAVINGCSV = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Original_30_Brexit_Clean.csv'
SAVINGTXT = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Original_30_Brexit_Clean.txt'

txt_file = open(SAVINGTXT, 'w+')

resdf = pd.DataFrame(columns = ['prolific_id', 'political_affiliation', 'opinion'])

for (pid, pa, p_opinion) in zip(data[PID], data[PA], data['Opinion']):

    p_opinion_list = p_opinion.split(".")

    temp_list = []
    for s in p_opinion_list :

        if s == '' or s == ' ' or s == '  ':
            continue 
        else :
            stripped = s.strip()
            temp_list.append(stripped)
            txt_file.write(stripped + "\n\n")

    ith = [pid, pa, temp_list]
    resdf.loc[len(resdf)] = ith 
    
txt_file.close()
resdf.to_csv(SAVINGCSV, index = False)
