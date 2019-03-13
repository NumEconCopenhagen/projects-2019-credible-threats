import numpy as np
import pandas as pd
#import os

filename = 'imdb.csv'

test = pd.read_csv(filename, sep=';', encoding='latin-1', escapechar='\\')

df = pd.DataFrame(test)

for i in range(44,48):
    df.drop(columns=[f'Unnamed: {i}'], inplace=True)

df.drop(columns=['fn','tid','wordsInTitle','url'], inplace=True)
I = df['imdbRating']
print(df.head(10))



