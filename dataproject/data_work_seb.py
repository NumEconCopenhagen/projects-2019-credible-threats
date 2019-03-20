import matplotlib.pyplot as plt 
import matplotlib as ax
from data_gen_test import gen_df
import numpy as np


filename = 'imdb.csv'

df = gen_df(filename)
I = df['year']<1920
df.drop(df[I].index,inplace=True)
df['year'] = df['year'].astype(int)

fig,ax = plt.subplots()

# Plot year sum of different genres
for j,i in enumerate(['Action','Western','War','Animation'],1):
    y_sum = df.groupby('year')[i].sum()
    
    ax = plt.subplot(2,2,j)
    y_sum.plot(kind='bar', color='black')

    n = 10  # Keeps every 10th label
    [l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]

    plt.xlabel('year')
    plt.ylabel(i)
    
#plt.show()

# Search for string in dataframe
print(list(df))
df['NomWinRatio'] = df['nrOfWins']/df['nrOfNominations']
I = df['NomWinRatio'] <= 0.2
#print(df.loc[I])
df.plot.scatter(x='NomWinRatio', y='nrOfNewsArticles')
plt.show()

#print(df[df['title'].str.contains('')])
#print(df['nrofNewsArticles'])