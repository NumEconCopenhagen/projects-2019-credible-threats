from data_gen_test import gen_df

filename = 'imdb.csv'

df = gen_df(filename)

print(df.head(10))
