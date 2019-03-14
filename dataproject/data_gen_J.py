import numpy as np
import pandas as pd
#import os

filename = 'imdb.csv'

test = pd.read_csv(filename, sep=';', encoding='latin-1', escapechar='\\')

df = pd.DataFrame(test)
print(df.shape)

for i in range(44,48):
    df.drop(columns=[f'Unnamed: {i}'], inplace=True)

df.drop(columns=['fn','tid','wordsInTitle','url'], inplace=True)
I = df['imdbRating']
print(df.shape)


I = df['type'] == 'video.movie'
df = df.loc[I]
df.drop(columns=['type'], inplace=True)
print(df.shape)

df.dropna(inplace=True)
print(df.shape)

df['imdbRating'] = df['imdbRating'].astype(str)
df['imdbRating'].replace(regex=True, inplace=True,to_replace='0',value='')
print(type(df['imdbRating'][0]))
df['imdbRating'] = df['imdbRating'].astype(float)

df['duration'] = df['duration']/60**2

test = np.array([1, 2, 3])

#df.to_excel('imdb_test.xlsx', index=False)
print(df.head(8))