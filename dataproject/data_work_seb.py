import matplotlib.pyplot as plt 
from data_gen_test import gen_df

filename = 'imdb.csv'

df = gen_df(filename)

plt.figure(1)

for j,i in enumerate(['Action','Western','War','Drama'],1):
    y_sum = df.groupby('year')[i].sum()
    print(j)

    plt.subplot(4,1,j)
    y_sum.plot(kind='bar')

    #plt.hist(y_sum[:])
    plt.xticks([])
    plt.xlabel('year')
    plt.ylabel(i)

plt.show()
