import pandas as pd
from summarizer import Summarizer, TransformerSummarizer

import warnings
warnings.filterwarnings("ignore")

DATASET = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Original_30_Brexit_Clean.txt'
SAVING =  '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Data_Algo_Summary_10/'
LIMIT = 10

# Load the data
data = pd.read_csv(DATASET, sep="\n\n", header=None)
data.columns = ['text']
final_data = '.\n'.join(data['text'])
final_data = final_data + "."

##### BERT 
bert_model = Summarizer()
bert_summary = bert_model(final_data, num_sentences=LIMIT)

# bert summary contains full stop at end
bert_summary = bert_summary[0:-1]
# rest of the full stops are eliminated by split fxn
bert_summary_split = bert_summary.split(". ")

file_bert = open(SAVING + '/BERT.txt', 'w+')

for sentence in bert_summary_split :
    file_bert.write(str(sentence) + "\n\n") 

file_bert.close()

print("BERT DONE")

##### GPT 2
GPT2_model = TransformerSummarizer(transformer_type="GPT2", transformer_model_key="gpt2-medium")
GPT2_summary = GPT2_model(final_data, num_sentences=LIMIT)

# gpt2 summary contains full stop at end
GPT2_summary = GPT2_summary[0:-1]
# rest of the full stops are eliminated by split fxn
GPT2_summary_split = GPT2_summary.split(". ")

file_GPT2 = open(SAVING + '/GPT2.txt', 'w+')

for sentence in GPT2_summary_split :
    file_GPT2.write(str(sentence) + "\n\n") 

file_GPT2.close()

print("GPT2 DONE")

#### XL Net
XLNet_model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")
XLNet_summary = XLNet_model(final_data, num_sentences=LIMIT)

# xlnet summary contains full stop at end
XLNet_summary = XLNet_summary[0:-1]
# rest of the full stops are eliminated by split fxn
XLNet_summary_split = XLNet_summary.split(". ")

file_XLNet = open(SAVING + '/XLNet.txt', 'w+')

for sentence in XLNet_summary_split :
    file_XLNet.write(str(sentence) + "\n\n") 

file_XLNet.close()

print("XLNET DONE")
