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
for j,i in enumerate(['Action','Western','War','Drama'],1):
    y_sum = df.groupby('year')[i].sum()
    
    ax = plt.subplot(2,2,j)
    y_sum.plot(kind='bar')

    n = 10  # Keeps every 10th label
    [l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]

    plt.xlabel('year')
    plt.ylabel(i)
    
plt.show()

print(df.head(10))
