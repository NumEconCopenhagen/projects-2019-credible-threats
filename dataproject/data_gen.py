import numpy as np
import pandas as pd 
import os

filename = 'projects-2019-credible-threats\dataproject\imdb.csv'

test = pd.read_csv(filename, sep=';', encoding='latin-1', escapechar='\\')

df = pd.DataFrame(test)

for i in range(44,48):
    df.drop(columns=[f'Unnamed: {i}'], inplace=True)

df.drop(columns=['fn','tid','wordsInTitle','url'], inplace=True)


mean_df = df.groupby('year')['imdbRating'].mean()
print(mean_df)