import pandas as pd
import scipy.stats

ROUGE = [0.292, 0.307, 0.403, 0.334, 0.345, 0.335, 0.44]
# ROUGE = [0.799, 0.791, 0.82, 0.803, 0.806, 0.803, 0.828]
# ROUGE = [0.569, 0.563, 0.584, 0.573, 0.575, 0.574, 0.591]
# AUTHOR = [6.188, 6.188, 5.688, 4.625, 5.188, 5.688, 5.438]
CROSSEM_S = [0.183, 0.148, 0.167, 0.15, 0.132, 0.188, 0.163]
# CROSSEM_BERT = [0.721, 0.711, 0.734, 0.711, 0.722, 0.723, 0.724]

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

# SAVING = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Data_Correlation/Correlation_Vaccine.csv'
# df = pd.DataFrame(main_list, columns=cols) 
# df.to_csv(SAVING, index=True) 

rcs = round(scipy.stats.pearsonr(ROUGE, CROSSEM_S)[0],4)
print(rcs)

rcs = round(scipy.stats.spearmanr(ROUGE, CROSSEM_S)[0],4)
print(rcs)

rcs = round(scipy.stats.kendalltau(ROUGE, CROSSEM_S)[0],4)
print(rcs)