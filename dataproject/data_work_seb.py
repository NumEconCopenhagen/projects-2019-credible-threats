import matplotlib.pyplot as plt 
from data_gen import gen_df
import numpy as np
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


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

    # Get English titles 
    top_id = top.tid.tolist()[0:10]
    bottom_id = bottom.tid.tolist()[0:10]
    id_list = top_id + bottom_id

    eng_names = []
    
    for i,id in enumerate(id_list):
        print(id)
        test = requests.get('https://www.imdb.com/title/' + id)
        soup = bs(test.text,'html.parser')
        if soup.find('div',class_='originalTitle') != None:
            eng_names.append(soup.find('div',class_='originalTitle').text)
        else:
            eng_names.append(soup.find('h1').text)
        print(i)

    df_merge = pd.DataFrame(i for i in eng_names)
    
    df_merge.rename(columns={'0': 'tid'})

    #test = df.merge(df_merge,how='right',on='tid')
    #print(test.head())


top_bottom_movies(df)