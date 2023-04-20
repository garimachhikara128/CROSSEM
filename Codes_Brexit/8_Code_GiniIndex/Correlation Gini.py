import pandas as pd
import scipy.stats

ROUGE = [0.192, 0.105, 0.129, 0.092, 0.183, 0.178, 0.162]
BERT = [0.018, 0.012, 0.013, 0.01, 0.02, 0.018, 0.019]
AUTHOR = [0.179, 0.247, 0.292, 0.245, 0.151, 0.164, 0.165]
CROSSEM_S = [0.141, 0.117, 0.119, 0.124, 0.131, 0.129, 0.151]

cols = ["ROUGE & AUTHOR", "BERT & AUTHOR", "CROSSEM-S & AUTHOR"]
main_list = []

ra = round(scipy.stats.spearmanr(ROUGE, AUTHOR)[0],4)
ba = round(scipy.stats.spearmanr(BERT, AUTHOR)[0],4)
csa = round(scipy.stats.spearmanr(CROSSEM_S, AUTHOR)[0],4)

print("SPEARMAN")
print("ROUGE & AUTHOR", ra)
print("BERT & AUTHOR", ba)
print("CROSSEM-S & AUTHOR", csa)
print("\n")

ra = round(scipy.stats.kendalltau(ROUGE, AUTHOR)[0],4)
ba = round(scipy.stats.kendalltau(BERT, AUTHOR)[0],4)
csa = round(scipy.stats.kendalltau(CROSSEM_S, AUTHOR)[0],4)

print("KENDALLTAU")
print("ROUGE & AUTHOR", ra)
print("BERT & AUTHOR", ba)
print("CROSSEM-S & AUTHOR", csa)