from json.tool import main
from tracemalloc import start
from xml.etree.ElementTree import PI
import pandas as pd

PID = 'Please enter your Prolific ID'

SAVINGTXT = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Data_Human_Summary'
data1 = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Data_Human_Summary/Summary_Vaccine_For.csv')

for i, p_opinion in enumerate(data1['Opinion'], start=1):

    txt_file = open(SAVINGTXT + "/" + "F" + str(i) + ".txt", 'w+')
    p_opinion_list = p_opinion.split(".")

    temp_list = []
    for s in p_opinion_list :

        if s == '' or s == ' ' or s == '  ':
            continue 
        else :
            stripped = s.strip()
            temp_list.append(stripped)
            txt_file.write(stripped + "\n\n")
            print(stripped)

        
    txt_file.close()


## ============================================================================================================ ##

data1 = pd.read_csv('/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Data_Human_Summary/Summary_Vaccine_Against.csv')

for i, p_opinion in enumerate(data1['Opinion'], start=1):

    txt_file = open(SAVINGTXT + "/" + "A" + str(i) + ".txt", 'w+')
    p_opinion_list = p_opinion.split(".")

    temp_list = []
    for s in p_opinion_list :

        if s == '' or s == ' ' or s == '  ':
            continue 
        else :
            stripped = s.strip()
            temp_list.append(stripped)
            txt_file.write(stripped + "\n\n")
            print(stripped)

    txt_file.close()
