
#filename = 'imdb.csv'

#df = gen_df(filename)



def _plot_1(df,genre,timevar):

    df['count'] = 1
    df['movies_year'] = df.groupby(timevar)['count'].transform(lambda x: x.sum())  

    # Plot year sum of different genres
    for i in genre:

        # Calculate sum of movies by timevariable, and share of movies within time that is of a certain genre
        df[f'{i}_time'] = df.groupby(timevar)[i].transform(lambda x: x.sum())
        df[f'{i} share'] = df[f'{i}_time']/df['movies_year']

        # Take first element of each timevariable group
        y_share = df.groupby(timevar)[f'{i} share'].first()

        # Plot the first eleents
        y_share.plot(kind='line', sharex='col', sharey='row')


        # Add labels and title
        plt.xlabel(timevar)
        plt.ylabel('share of movies')
        if len(genre) == 1:
            plt.title(i)
        if len(genre) > 1:
            plt.legend(loc='upper left')

    #plt.show()

def plot_1(df):

    widgets.interact(_plot_1,
                    df = widgets.fixed(df),
                    genre = widgets.SelectMultiple(
                        options = genre_list,
                        description = 'Genres',
                        disabled = False),
                    timevar = widgets.Dropdown(
                    options = ['year', 'decade'],
                    description = 'Timevariable',
                    disabled = False))

plot_1(df)
