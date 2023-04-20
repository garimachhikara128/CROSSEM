import clusterrank
summarizer = clusterrank.ClusterRank()
pathToFile = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Vaccine/Original_30_Vaccine_Clean.txt'
summary = summarizer.summarizeFile(pathToFile)

print(summary)