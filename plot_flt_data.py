import pandas as pd
import os.path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import matplotlib as mpl
import seaborn as sns




df=pd.read_csv(os.path.dirname(__file__)+'/flights_fet_sel.csv')
result=df
#Get first 10 rows
df=df.head(10)
#create airport dict from actual and scheduled airports
airports = df.set_index('ACTL_DPRT_ARPT_CD')['SCH_DPRT_ARPT_CD'].to_dict()



# function to get main and max count
def get_min_max(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}


# Creation of a dataframe with statitical infos on each airline:
airport_stats = df['DPRT_TIME_DELAY'].groupby(df['SCH_DPRT_ARPT_CD']).apply(get_min_max).unstack()
airport_stats = airport_stats.sort_values('count')


font = {'family' : 'STIXGeneral', 'weight' : 'bold', 'size'   : 12}
mpl.rc('font', **font)


# I extract a subset of columns and redefine the airlines labeling 
df2 = df.loc[:, ['SCH_DPRT_ARPT_CD', 'DPRT_TIME_DELAY']]
df2['SCH_DPRT_ARPT_CD'] = df2['SCH_DPRT_ARPT_CD'].replace(airports)

colors = ['royalblue', 'grey', 'wheat', 'c', 'firebrick', 'seagreen', 'lightskyblue',
          'lightcoral', 'yellowgreen', 'gold', 'tomato', 'violet', 'aquamarine', 'chartreuse']

fig = plt.figure(1, figsize=(16,15))
gs=GridSpec(2,2)             
ax1=fig.add_subplot(gs[0,0]) 
ax2=fig.add_subplot(gs[0,1]) 
ax3=fig.add_subplot(gs[1,:]) 


# Pie chart by scheduled departure airport
labels = [s for s in  airport_stats.index]
sizes  = airport_stats['count'].values
explode = [0.3 if sizes[i] < 20000 else 0.0 for i in range(len(airports))]
patches, texts, autotexts = ax1.pie(sizes, explode = explode,
                                labels=labels, colors = colors,  autopct='%1.0f%%',
                                shadow=False, startangle=0)
for i in range(len(airports)): 
    texts[i].set_fontsize(14)
ax1.axis('equal')
ax1.set_title('% of flights per Airport', bbox={'facecolor':'midnightblue', 'pad':5},
              color = 'w',fontsize=18)

# set legand by Airport
comp_handler = []
for i in range(len(airports)): 
    comp_handler.append(mpatches.Patch(color=colors[i],
            label = airport_stats.index[i] + ': ' + airports[airport_stats.index[i]]))
ax1.legend(handles=comp_handler, bbox_to_anchor=(0.2, 0.9), 
           fontsize = 13, bbox_transform=plt.gcf().transFigure)


# Pie chart by mean  dealy at departure airport 
sizes  = airport_stats['mean'].values
sizes  = [max(s,0) for s in sizes]
explode = [0.0 if sizes[i] < 20000 else 0.01 for i in range(len(airports))]
patches, texts, autotexts = ax2.pie(sizes, explode = explode, labels = labels,
                                colors = colors, shadow=False, startangle=0,
                                autopct = lambda p :  '{:.0f}'.format(p * sum(sizes) / 100))
for i in range(len(airports)): 
    texts[i].set_fontsize(14)
ax2.axis('equal')
ax2.set_title('Mean delay at origin', bbox={'facecolor':'midnightblue', 'pad':5},
              color='w', fontsize=18)


# Plot that shows departure delay vs departure airport
colors = ['firebrick', 'gold', 'lightcoral', 'aquamarine', 'c', 'yellowgreen', 'grey',
          'seagreen', 'tomato', 'violet', 'wheat', 'chartreuse', 'lightskyblue', 'royalblue']

ax3 = sns.stripplot(y="SCH_DPRT_ARPT_CD", x="DPRT_TIME_DELAY", size = 4, palette = colors,
                    data=df2, linewidth = 0.5,  jitter=True)
plt.setp(ax3.get_xticklabels(), fontsize=14)
plt.setp(ax3.get_yticklabels(), fontsize=14)
ax3.set_xticklabels(['{:2.0f}h{:2.0f}m'.format(*[int(y) for y in divmod(x,3600)])
                         for x in ax3.get_xticks()])
plt.xlabel('Departure delay', fontsize=18, bbox={'facecolor':'midnightblue', 'pad':5},
           color='w', labelpad=20)
ax3.yaxis.label.set_visible(False)
ax3.set_facecolor('lightgray')
plt.tight_layout(w_pad=3) 



#departure airport count
origin_nb = dict()
for carrier in airports.keys():
    liste_origin_airport = df[df['SCH_DPRT_ARPT_CD'] == carrier]['SCH_DPRT_ARPT_CD'].unique()
    origin_nb[carrier] = len(liste_origin_airport)
    
test_df = pd.DataFrame.from_dict(origin_nb, orient='index')
test_df.rename(columns = {0:'count'}, inplace = True)
ax = test_df.plot(kind='bar', figsize = (8,3))
labels = [airports[item.get_text()] for item in ax.get_xticklabels()]
ax.set_xticklabels(labels)
plt.ylabel('Number of airports visited', fontsize=14, weight = 'bold', labelpad=12)
plt.setp(ax.get_xticklabels(), fontsize=11, ha = 'right', rotation = 80)
ax.legend().set_visible(False)
plt.show()    


