# importing package
import pandas as pd
import matplotlib.pyplot as plt

# create data
df1 = pd.DataFrame([['BREXIT', -0.4404 , -0.018 , -0.2477 , 0.3], 
                   ['VACCINE', -0.491, -0.5597,	-0.491,	0.4001], 
                   ['RECRUITMENT', -0.4, -0.0721, -0.3612, 0.2727]],
                   columns=['Spearman', 'ROUGE', 'BertScore', 'MoverScore', 'CROSSEM-s'])
df2 = pd.DataFrame([['BREXIT',-0.3591,	0	,-0.2052	,0.25], 
                   ['VACCINE', -0.3504,	-0.4104,	-0.3504	,0.3504], 
                   ['RECRUITMENT',-0.35	,-0.0976,	-0.2635,	0.15]],
                  columns=['Kendall Tau', 'ROUGE', 'BertScore', 'MoverScore', 'CROSSEM-s'])
# view data
# print(df)

hatch = [ "/","/","/", "o","o","o", "+","+","+", '.','.','.']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4.77))

# plot grouped bar chart
bars1 = df1.plot(x='Spearman',
        kind='bar',
        stacked=False,
        grid=True,
        ylim = (-0.6,0.6),
        rot=0,
        color = ['cyan', 'wheat', 'darkgray', 'palegreen'],
        width = 0.75,
        ax=axes[0],
        legend = False,
        fontsize = 12
        )
bars1.set_ylabel('Correlation with average author rating', fontdict={'fontsize':15})
bars1.set_xlabel('Spearman', fontdict={'fontsize':15})

i = 0
for patch in bars1.patches:
   patch.set_hatch(hatch[i])
   i = i + 1

# plot grouped bar chart
bars2 = df2.plot(x='Kendall Tau',
        kind='bar',
        stacked=False,
        grid=True,
        ylim = (-0.6,0.6),
        rot=0,
        color = ['cyan', 'wheat', 'darkgray', 'palegreen'],
        width = 0.75,
        ax=axes[1],
        fontsize = 12,
        legend = False,
        )
# bars2.set_ylabel('Correlation with average author rating', fontdict={'fontsize':13})
bars2.set_xlabel('Kendall Tau', fontdict={'fontsize':15})

i = 0
for patch in bars2.patches:
   patch.set_hatch(hatch[i])
   i = i + 1

plt.legend(loc = "upper left")
plt.savefig("fig.pdf", format="pdf", bbox_inches="tight")
plt.show()