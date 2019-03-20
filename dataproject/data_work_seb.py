import matplotlib.pyplot as plt 
from data_gen import gen_df
import numpy as np


filename = 'imdb.csv'

df = gen_df(filename)
df['year'] = df['year'].astype(int)

def plot_1(df):

    fig,ax = plt.subplots()

    # Plot year sum of different genres
    for j,i in enumerate(['Action','Western','War','Animation'],1):
        y_sum = df.groupby('year')[i].sum()
        
        ax = plt.subplot(2,2,j)
        y_sum.plot(kind='bar', color='black')

        # Keeps every 10th label
        n = 10  
        [l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]

        plt.xlabel('year')
        plt.ylabel(i)
        
    plt.show()

def plot_2(df):
    df['NomWinRatio'] = df['nrOfWins']/df['nrOfNominations']

    genre_list = ['Action','Animation']

    for i in genre_list:
        I = df[i] == 1

        x = df.loc[I, 'ratingCount']
        y = df.loc[I, 'nrOfWins']

        plt.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x: '{:,}').format(int(x)))

    plt.legend(loc='upper')
    plt.show()

plot_2(df)
#print(df.ratingCount.head())