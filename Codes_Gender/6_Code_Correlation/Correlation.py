from curses.ascii import CR
import pandas as pd
 
# df = {
#   "ROUGE": [0.314, 0.332, 0.324, 0.246, 0.218, 0.314, 0.286],
#   "AUTHOR": [6.74, 6.42, 6.16, 6.84, 6.26, 7.42, 6.84],
#   "CROSSEM": [0.219, 0.136, 0.232, 0.151, 0.165, 0.219, 0.18]
# }
 
# data = pd.DataFrame(df)
 
# print(data.corr())

import scipy.stats

# ROUGE = [0.314, 0.332, 0.324, 0.246, 0.218, 0.314, 0.286]
# ROUGE = [0.818, 0.815, 0.828, 0.802, 0.785, 0.817, 0.804]
ROUGE = [0.58, 0.59, 0.59, 0.57, 0.56, 0.58, 0.57]
# AUTHOR = [6.74, 6.42, 6.16, 6.84, 6.26, 7.42, 6.84]
AUTHOR = [6.95, 6.41, 6.45, 7.14, 6.45, 7.59, 7.05]
CROSSEM = [0.759, 0.741, 0.773, 0.748, 0.747, 0.756, 0.756]

print("\nPEARSON RESULTS :-")

print("ROUGE and AUTHOR" , scipy.stats.pearsonr(ROUGE, AUTHOR)[0])
print("ROUGE and CROSSEM" , scipy.stats.pearsonr(ROUGE, CROSSEM)[0])
print("AUTHOR and CROSSEM" , scipy.stats.pearsonr(AUTHOR, CROSSEM)[0])

print("\nSPEARMAN RESULTS :-")

print("ROUGE and AUTHOR" , scipy.stats.spearmanr(ROUGE, AUTHOR)[0])
print("ROUGE and CROSSEM" , scipy.stats.spearmanr(ROUGE, CROSSEM)[0])
print("AUTHOR and CROSSEM" , scipy.stats.spearmanr(AUTHOR, CROSSEM)[0])

print("\nKENDALLTAU RESULTS :-")

print("ROUGE and AUTHOR" , scipy.stats.kendalltau(ROUGE, AUTHOR)[0])
print("ROUGE and CROSSEM" , scipy.stats.kendalltau(ROUGE, CROSSEM)[0])
print("AUTHOR and CROSSEM" , scipy.stats.kendalltau(AUTHOR, CROSSEM)[0])
