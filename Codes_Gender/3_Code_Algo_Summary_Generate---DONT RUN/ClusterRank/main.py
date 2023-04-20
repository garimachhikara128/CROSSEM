import clusterrank
summarizer = clusterrank.ClusterRank()
pathToFile = "/Users/garima/Desktop/Self/PhD/Research Work/Fairness in Summarization/Codes/Gender_30_Data_Sentences.txt"
summary = summarizer.summarizeFile(pathToFile)

print(summary)