# Stjæler lidt kode fra Seb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as widgets

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


#####################################################################################
# Data pjat 

# Data types 
print(df.dtypes)

# Summary Statistics 
print(df[["year", "imdbRating", "duration", "nrOfWins", "nrOfNominations"]].describe())


# Generating genre list
genre = ['Action', 'Adult', 'Adventure', 'Animation', 'Biography',
         'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy',
         'FilmNoir', 'GameShow', 'History', 'Horror', 'Music', 'Musical',
         'Mystery', 'News', 'RealityTV', 'Romance', 'SciFi', 'Short', 'Sport',
         'TalkShow', 'Thriller', 'War', 'Western']


# Counting movies in each genre
for i in genre: 
    sum = df[i].sum(axis=0)
    print(f'Sum of {i}: {sum:.0f}')


#####################################################################################
# Figures
#####################################################################################

# Histogram
import seaborn as sns
sns.set()

# plt.hist(df["imdbRating"], bins=10)


# Histogram by genre
df_hist = df.loc[df["Comedy"] == 1]
plt.hist(df_hist["imdbRating"], bins=10)


# Interactive Histogram
def histogram(variable, genre, bins_num):
        df_hist = df.loc[df[genre] == 1]
        plt.hist(df_hist[variable], bins=bins_num)
    
        # Labels
        plt.title("Histogram")
        plt.ylabel("Number")
        plt.xticks(range(1,11))
    
# histogram("imdbRating", "Comedy")   # Remember quote marks around variable names
# Consider writing an error code indicating to use quote marks


def hist_interactive(variable): 
    widgets.interact(histogram, 
    variable = widgets.fixed(variable), 
    
    # Genre Dropdown
    genre = widgets.Dropdown(
    description="Genre", 
    options=genre, 
    value="Comedy"),
    
    # Bins slider 
    bins_num=widgets.IntSlider(
    value=10,
    description="Bins", 
    min=1,
    max=50, 
    step=1,
    disabled=False,
    continuous_update=False)
    ); 

hist_interactive("imdbRating")

#####################################################################################

# Scatter X against years
def scatter(variable):
    plt.figure(figsize=(11,8))
    plt.scatter(df['year'], variable)
    
    plt.title("Scatterplot")
    plt.xlabel("Year")

scatter(df["imdbRating"])    


print(df[df["nrOfWins"] == 137])
print(df[df["nrOfNominations"] == 137])

