import clusterrank
summarizer = clusterrank.ClusterRank()
pathToFile = '/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes_Brexit/Original_30_Brexit_Clean.txt'
summary = summarizer.summarizeFile(pathToFile)

print(summary)