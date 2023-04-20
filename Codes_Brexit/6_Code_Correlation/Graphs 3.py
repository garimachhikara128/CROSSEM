# importing package
import pandas as pd
import matplotlib.pyplot as plt

# create data
df = pd.DataFrame([['Brexit', -0.4404 , -0.018 , -0.2477 , 0.3], 
                   ['Vaccine', -0.491, -0.5597,	-0.491,	0.4001], 
                   ['Recruitment', -0.4, -0.0721, -0.3612, 0.2727]],
# df = pd.DataFrame([['Brexit',-0.3591,	0	,-0.2052	,0.25], 
#                    ['Vaccine', -0.3504,	-0.4104,	-0.3504	,0.3504], 
#                    ['Recruitment',-0.35	,-0.0976,	-0.2635,	0.15]],
                  columns=['Surveys', 'ROUGE', 'BertScore', 'MoverScore', 'CROSSEM'])
# view data
print(df)

hatch = [ "/","/","/", "o","o","o", "+","+","+", '.','.','.']

# plot grouped bar chart
bars = df.plot(x='Surveys',
        kind='bar',
        stacked=False,
        grid=True,
        ylim = (-0.6,0.6),
        rot=0,
        color = ['cyan', 'wheat', 'darkgray', 'palegreen'],
        width = 0.75,
        legend = False,
        fontsize = 20,
        )
bars.set_ylabel('ρ with avg. author score', fontdict={'fontsize':21})
# bars.set_ylabel('τ with avg. author score', fontdict={'fontsize':21})
bars.set_xlabel('', fontdict={'fontsize':0})

i = 0
for patch in bars.patches:
   patch.set_hatch(hatch[i])
   i = i + 1

# plt.legend(ncol = 2, loc = "upper right", fontsize = 14)
plt.savefig("spearman.pdf", format="pdf", bbox_inches="tight")
plt.show()