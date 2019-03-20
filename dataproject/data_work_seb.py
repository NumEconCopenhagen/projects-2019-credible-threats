import matplotlib.pyplot as plt 
from data_gen import gen_df
import numpy as np


filename = 'imdb.csv'

df = gen_df(filename)
df['year'] = df['year'].astype(int)

def plot_1(df):
    
    df['count'] = 1
    df['movies_year'] = df.groupby('year')['count'].transform(lambda x: x.sum())  

    # Plot year sum of different genres
    for j,i in enumerate(['Crime','Western','War','Biography'],1):
        df[f'{i}_year'] = df.groupby('year')[i].transform(lambda x: x.sum())
        df[f'{i}_share'] = df[f'{i}_year']/df['movies_year']

        y_share = df.groupby('year')[f'{i}_share'].first()
        
        ax = plt.subplot(2,2,j)
        y_share.plot(kind='line', color='black', sharex='col', sharey='row')

        # Keeps every 10th label
        #n = 10  
        #[l.set_visible(False) for (i,l) in enumerate(ax.xaxis.get_ticklabels()) if i % n != 0]

        plt.xlabel('year')
        plt.ylabel('share of movies')
        plt.title(i)
        
    plt.show()

def plot_2(df):
    df['NomWinRatio'] = df['nrOfWins']/df['nrOfNominations']

    genre_list = ['Action','Animation']

    for i in genre_list:
        I = df[i] == 1

        x = df.loc[I, 'ratingCount']
        y = df.loc[I, 'nrOfWins']

    plt.legend(loc='upper')
    plt.show()

def top_bottom_movies(df):
    # Condition on minimum number of ratings
    I = df['ratingCount'] >= 2000

    top = df.sort_values('imdbRating', ascending=False)[I]
    bottom = df.sort_values('imdbRating', ascending=True)[I]
    print(top.head(3), bottom.head(3))


top_bottom_movies(df)