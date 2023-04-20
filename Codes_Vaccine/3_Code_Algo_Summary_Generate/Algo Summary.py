import numpy as np
import pandas as pd
import nltk 
from sklearn.feature_extraction.text import CountVectorizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from collections import Counter
from functools import reduce

import warnings
warnings.filterwarnings("ignore")

DATASET = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Original_30_Vaccine_Clean.txt'
SAVING =  '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Data_Algo_Summary_10/'
LIMIT = 10

def lin(V, m, lamb):
        '''DSDR with linear reconstruction
        Parameters
        ==========
        - V : 2d array_like, the candidate data set
        - m : int, the number of sentences to be selected
        - lamb : float, the trade off parameter
        Returns
        =======
        - L : list, the set of m summary sentences indices
        '''
        L = []
        V = np.array(V)
        B = np.dot(V, V.T) / lamb
        n = len(V)
        for t in range(m):
            scores = []
            for i in range(n):
                score = np.sum(B[:,i] ** 2) / (1. + B[i,i])
                scores += [(score, i)]
            max_score, max_i = max(scores)
            L += [max_i]
            B = B - np.outer(B[:,max_i], B[:,max_i]) / (1. + B[max_i,max_i])
        return L

    
def non(V, gamma, eps=1.e-8):
        '''DSDR with nonnegative linear reconstruction     
        Parameters
        ==========
        - V : 2d array_like, the candidate sentence set
        - gamma : float, > 0, the trade off parameter
        - eps : float, for converge
        Returns
        =======
        - beta : 1d array, the auxiliary variable to control candidate sentences
            selection
        '''
        V = np.array(V)
        n = len(V)
        A = np.ones((n,n))
        beta = np.zeros(n)
        VVT = np.dot(V, V.T) # V * V.T
        np.seterr(all='ignore')
        while True:
            _beta = np.copy(beta)
            beta = (np.sum(A ** 2, axis=0) / gamma) ** .5
            while True:
                _A = np.copy(A)
                A *= VVT / np.dot(A, VVT + np.diag(beta))
                A = np.nan_to_num(A) # nan (zero divide by zero) to zero
                if np.sum(A - _A) < eps: break
            if np.sum(beta - _beta) < eps: break
        return beta

# Load the data
data = pd.read_csv(DATASET, sep="\n\n", header=None)
data.columns = ['text']
print(data)

# Convert word to vectors
count_vectorizer = CountVectorizer(stop_words='english') 
cv = count_vectorizer.fit_transform(data['text'])
print(cv.shape)
V = cv.toarray()
# type(V)

# 4. DSDR Linear
L = lin(V, m=LIMIT, lamb=0.1)
# print(L)

columns=count_vectorizer.get_feature_names_out()

file_dsdr_lin = open(SAVING + '/DSDRLin.txt', 'w+')

for i in L:
  file_dsdr_lin.write(data.iloc[i]['text'] + "\n\n") 

file_dsdr_lin.close()

# 5. DSDR Non Linear
beta = non(V, gamma=0.1)

file_dsdr_non_lin = open(SAVING + '/DSDRNonLin.txt', 'w+')

i = 1
for score, v, content in sorted(zip(beta, V, data['text']), reverse=True, key = lambda x: x[0]):

  if i > LIMIT :
    break

  file_dsdr_non_lin.write(content + "\n\n") 
  i += 1 

file_dsdr_non_lin.close()

# 6. Lex Rank

summarizer_lex = LexRankSummarizer()

s = ''  
for ps in data['text'] :
  s += ps + '\n\n'

parser = PlaintextParser.from_string(s, Tokenizer("english"))

# Summarize using sumy LexRank
summary_lex = summarizer_lex(parser.document, LIMIT)

file_lex_rank = open(SAVING + '/LexRank.txt', 'w+')

for sentence in summary_lex :
    file_lex_rank.write(str(sentence) + "\n\n") 

file_lex_rank.close()

# 7. LSA

summarizer_lsa = LsaSummarizer()

# Summarize using sumy LSA
summary_lsa = summarizer_lsa(parser.document, LIMIT)

file_lsa = open(SAVING + '/LSA.txt', 'w+')

for sentence in summary_lsa :
    file_lsa.write(str(sentence) + "\n\n") 

file_lsa.close()

# 8. LUHN
summarizer_luhn = LuhnSummarizer()
summary_luhn = summarizer_luhn(parser.document,LIMIT)

file_luhn = open(SAVING + '/LUHN.txt', 'w+')

for sentence in summary_luhn :
    file_luhn.write(str(sentence) + "\n\n") 

file_luhn.close()

# 9. SUM BASIC

def count_words(texts):
	"""
	Counts the words in the given texts, ignoring puncuation and the like.
	@param texts - Texts (as a single string or list of strings)
	@return Word count of texts
	"""

	if type(texts) is list:
		return len(texts)

	return len(texts.split())

def sumbasic_summarize(limit, data, update):  
  
    data_list = data.apply(lambda x: x.split())

    # Counter for all words.
    cnts = Counter()
    for sent in data_list :
        cnts += Counter(sent)

    # Number of tokens.
    N = float(sum(cnts.values()))

    # Unigram probabilities.
    probs = {w: cnt / N for w, cnt in cnts.items()}

    # print(probs)

    # List of all sentences in all documents.
    sentences = data.tolist()

    # print(len(sentences))

    summary = []
    # Add sentences to the summary until there are no more sentences or word
    # limit is exceeded.
    while len(sentences) > 0 and len(summary) < limit:
        # Track the max probability of a sentence with corresponding sentence.
        max_prob, max_sent = 0.0, None

        for i, sent in enumerate(sentences):
            prob = 1 
            for w in data_list[i] : 
                prob *= probs[w] 
            
            if max_prob < prob:
                max_prob, max_sent = prob, sent

        if len(max_sent) > 0 :
            summary.append(max_sent)

        sentences.remove(max_sent)

        if update:
            # Apply the update for non-redundancy.
            for w in data_list[i]:
                probs[w] = probs[w] ** 2
  
    return summary 

summary_sumbasic = sumbasic_summarize(LIMIT, data['text'],update=False)

file_sum_basic = open(SAVING + '/SummBasic.txt', 'w+')

for sentence in summary_sumbasic :
    file_sum_basic.write(str(sentence) + "\n\n") 

file_sum_basic.close()
