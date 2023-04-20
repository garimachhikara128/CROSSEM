import pandas as pd
import scipy.stats

ROUGE = [0.161, 0.174, 0.06, 0.11, 0.089, 0.13, 0.098]
BERT = [0.013, 0.017, 0.011, 0.014, 0.008, 0.013, 0.021]
AUTHOR = [0.214, 0.208, 0.227, 0.272, 0.251, 0.2, 0.262]
CROSSEM_S = [0.198, 0.219, 0.135, 0.227, 0.138, 0.191, 0.145]

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