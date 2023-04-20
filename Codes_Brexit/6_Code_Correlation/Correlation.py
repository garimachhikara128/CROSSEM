import pandas as pd
import scipy.stats

ROUGE = [0.265, 0.284, 0.344, 0.333, 0.342, 0.284, 0.342]
# BERT = [0.791, 0.792, 0.8, 0.797, 0.801, 0.799, 0.808]
# MOVER = [0.563, 0.563, 0.575, 0.572, 0.572, 0.569, 0.58]
# AUTHOR = [6.375, 5.708, 4.5, 5.167, 6.083, 5.875, 6.083]
CROSSEM_S = [0.23, 0.191, 0.202, 0.158, 0.158, 0.229, 0.2]
# CROSSEM_BERT = [0.727, 0.723, 0.729, 0.72, 0.72, 0.729, 0.732]

cols = ["ROUGE & AUTHOR", "ROUGE & CROSSEM-S", "AUTHOR & CROSSEM-S", "ROUGE & CROSSEM-BERT", "AUTHOR & CROSSEM-BERT"]
main_list = []

# ra = round(scipy.stats.pearsonr(ROUGE, AUTHOR)[0],4)
# rcs = round(scipy.stats.pearsonr(ROUGE, CROSSEM_S)[0],4)
# acs = round(scipy.stats.pearsonr(AUTHOR, CROSSEM_S)[0],4)
# rcb = round(scipy.stats.pearsonr(ROUGE, CROSSEM_BERT)[0],4)
# acb = round(scipy.stats.pearsonr(AUTHOR, CROSSEM_BERT)[0],4)
# l1 = [ra, rcs, acs, rcb, acb]

# ra = round(scipy.stats.spearmanr(ROUGE, AUTHOR)[0],4)
# rcs = round(scipy.stats.spearmanr(ROUGE, CROSSEM_S)[0],4)
# acs = round(scipy.stats.spearmanr(AUTHOR, CROSSEM_S)[0],4)
# rcb = round(scipy.stats.spearmanr(ROUGE, CROSSEM_BERT)[0],4)
# acb = round(scipy.stats.spearmanr(AUTHOR, CROSSEM_BERT)[0],4)
# l2 = [ra, rcs, acs, rcb, acb]

# ra = round(scipy.stats.kendalltau(ROUGE, AUTHOR)[0],4)
# rcs = round(scipy.stats.kendalltau(ROUGE, CROSSEM_S)[0],4)
# acs = round(scipy.stats.kendalltau(AUTHOR, CROSSEM_S)[0],4)
# rcb = round(scipy.stats.kendalltau(ROUGE, CROSSEM_BERT)[0],4)
# acb = round(scipy.stats.kendalltau(AUTHOR, CROSSEM_BERT)[0],4)
# l3 = [ra, rcs, acs, rcb, acb]

# main_list.append(l1)
# main_list.append(l2)
# main_list.append(l3)

# SAVING = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Data_Correlation/Correlation_Brexit.csv'
# df = pd.DataFrame(main_list, columns=cols) 
# df.to_csv(SAVING, index=True) 

rcs = round(scipy.stats.pearsonr(ROUGE, CROSSEM_S)[0],4)
print(rcs)

rcs = round(scipy.stats.spearmanr(ROUGE, CROSSEM_S)[0],4)
print(rcs)

rcs = round(scipy.stats.kendalltau(ROUGE, CROSSEM_S)[0],4)
print(rcs)
