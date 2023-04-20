# importing package
import pandas as pd
import matplotlib.pyplot as plt

# create data
# df = pd.DataFrame([['BREXIT', -0.4404 , -0.018 , -0.2477 , 0.3], 
#                    ['VACCINE', -0.491, -0.5597,	-0.491,	0.4001], 
#                    ['RECRUITMENT', -0.4, -0.0721, -0.3612, 0.2727]],
df = pd.DataFrame([['BREXIT',-0.3591,	0	,-0.2052	,0.25], 
                   ['VACCINE', -0.3504,	-0.4104,	-0.3504	,0.3504], 
                   ['RECRUITMENT',-0.35	,-0.0976,	-0.2635,	0.15]],
                  columns=['Surveys', 'ROUGE', 'BertScore', 'MoverScore', 'CROSSEM-s'])
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
        )
bars.set_ylabel('Correlation with average author rating', fontdict={'fontsize':13})
bars.set_xlabel('Surveys', fontdict={'fontsize':13})

i = 0
for patch in bars.patches:
   patch.set_hatch(hatch[i])
   i = i + 1

plt.savefig("kendalltau.pdf", format="pdf", bbox_inches="tight")
plt.show()