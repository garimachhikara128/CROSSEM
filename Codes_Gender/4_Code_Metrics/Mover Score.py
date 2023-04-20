# !pip install git+https://github.com/AIPHES/emnlp19-moverscore.git
# !pip install transformers

from moverscore_v2 import get_idf_dict, word_mover_score 
from collections import defaultdict
from typing import List, Union, Iterable
from itertools import zip_longest
import numpy as np
import pandas as pd

LOCATION = 'MoverScore.csv'
human_summaries = ['F1', 'F2', 'F3', 'M1', 'M2', 'M3']
algo_summaries = ['ClusterRank', 'DSDRLin', 'DSDRNonLin', 'LexRank', 'SummBasic', 'LSA', 'LUHN', 'RNN_RNN']

main_list = []

def sentence_score(hypothesis: str, references: List[str], trace=0):
    
    idf_dict_hyp = defaultdict(lambda: 1.)
    idf_dict_ref = defaultdict(lambda: 1.)
    
    hypothesis = [hypothesis] * len(references)
    
    sentence_score = 0 

    scores = word_mover_score(references, hypothesis, idf_dict_ref, idf_dict_hyp, stop_words=[], n_gram=1, remove_subwords=False)
    
    sentence_score = np.mean(scores)
    
    if trace > 0:
        print(hypothesis, references, sentence_score)
            
    return sentence_score

def corpus_score(sys_stream: List[str],
                     ref_streams:Union[str, List[Iterable[str]]], trace=0):

    if isinstance(sys_stream, str):
        sys_stream = [sys_stream]

    if isinstance(ref_streams, str):
        ref_streams = [[ref_streams]]

    fhs = [sys_stream] + ref_streams

    corpus_score = 0
    for lines in zip_longest(*fhs):
        if None in lines:
            raise EOFError("Source and reference streams have different lengths!")
            
        hypo, *refs = lines
        corpus_score += sentence_score(hypo, refs, trace=0)
        
    corpus_score /= len(sys_stream)

    return corpus_score

for algo in algo_summaries :
        
        row_list = []
        for human in human_summaries :
            
            algo_summ_file = open('AS/' + algo + '.txt', 'r')
            algo_summ = algo_summ_file.read()
            human_summ_file = open('HS/' + human + '.txt', 'r')
            human_summ = human_summ_file.read()

            mover = corpus_score(algo_summ, human_summ)
            print(mover)
            row_list.append(round(mover,3))

        main_list.append(row_list)

df = pd.DataFrame(main_list, columns=human_summaries) 
df.to_csv(LOCATION, index=True) 
