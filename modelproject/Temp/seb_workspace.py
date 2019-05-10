import numpy as np
import pandas as pd
import itertools
import time
import scipy.optimize as optimize
from data_gen import gen_df 
import matplotlib.pyplot as plt
import math

result = math.sqrt(4)
print(result)

"""
n1 = 100
n2 = 10000

x1 = np.linspace(1,10,n1)
y1 = np.random.uniform(0,1,n1)

x2 = np.linspace(1,10,n2)
y2 = np.random.uniform(0,1,n2)

time1 = list()
time2 = list()

for i in range(5000):
        start1 = time.time()
        plt1 = plt.plot(x1,y1)
        end1 = time.time()-start1
        time1.append(end1)

for i in range(5000):
        start2 = time.time()
        plt2 = plt.plot(x2,y2)
        end2 = time.time()-start2
        time2.append(end2)


print(f'Plot with {n1} values: {sum(time1)/len(time1):.7f} seconds')
print(f'Plot with {n2} values: {sum(time2)/len(time2):.7f} seconds')
"""
"""
filename = 'imdb.csv'

df = gen_df(filename)

# Parameters
alphas = np.random.uniform(0,1,3)
betas = [1,2,3]

# Score-function for testing
def u_fun(xs,pars):
        util = xs.iloc[:,0]*pars[0]+xs.iloc[:,1]*pars[1]+xs.iloc[:,29]**pars[2]
        return 10*np.exp(util)/(1+np.exp(util))

# Building dataframe containing values for score-function
df_xs = pd.DataFrame()
df_xs = df.iloc[:,13:41]
df_xs['Duration'] = df['duration']
df_xs['Rating'] = df['imdbRating']

# Function that calculates minimum squared distance
def obj_fun(df_xs,pars):
        df_xs['Est_rating'] = u_fun(df_xs,pars)
        df_xs['Difference'] = (df_xs['Rating']-df_xs['Est_rating'])**2
        #print(df_xs[['Est_rating','Rating','Difference']].head())
        return df_xs['Difference'].sum()

# Testing from here
obj_fun(df_xs,alphas)
obj_fun(df_xs,[0,0,0])

min_fun = lambda a: obj_fun(df_xs,a)

bnds = ((0,None),(0,None),(0,None))

result = optimize.minimize(min_fun,alphas,method='SLSQP')


print(alphas,result.x)

print(obj_fun(df_xs,alphas),obj_fun(df_xs,result.x))

"""

"""
n = 300

#A1 = np.random.uniform(1,20,size=n)
#A2 = np.linspace(0,10,n)
#A3 = np.linspace(0,10,n)
start = time.time()

A1_grid, A2_grid, A3_grid = np.meshgrid(A1,A2,A3,indexing='ij')
A=A1_grid+A2_grid+A3_grid
print(np.max(A))

end = time.time()-start

print(f'{end:3.f} seconds')

iterator = itertools.combinations(A1, 3)

high = 0
time_list = list()

for k in range(10):

        start = time.time()

        iterator = itertools.combinations(enumerate(A1), 3)
        for i in iterator:
            print(i,i[0:],i[1:])
            
            test1 = i[1][0]/i[1][1]+i[1][2]
            test2 = i[0]*i[1]*i[2]
            
        if test2 < 20:
                if test1 > high:
                        high = test1
                        high_i = i
                        
        if j%100000 == 0:
                part = time.time()-start
                print(f'Iteratrion: {j} after {part:.2f} seconds')
        
        end = time.time()-start
        time_list.append(end)

avg = sum(time_list)/len(time_list)
print(f'{avg:.3f} seconds')

#print(f'{end:.3f} seconds, highest value is {high:.3f} with i: {high_i}')

for k in range(1,4):
    start = time.time()

    list_1 = np.random.uniform(1,20,size=n)
    list_2 = np.random.uniform(1,5,size=n)

    iterator = itertools.combinations(enumerate(list_2), 3)

    hi = 0
    indeces = list()

    for i in iterator:
        duration = sum([j[1] for j in i])        
        if duration >= 12 and duration <= 14:
            score = sum([list_1[j[0]] for j in i])
            if score > hi:
                hi = score
                dur = duration
                indeces = [j[0] for j in i]

    end = time.time() - start

    text = f'Highest value is {hi:.2f} \n'
    text += f'The duration is {dur:.2f} \n'
    text += f'This took {end:.1f} seconds'

    print(f'Iteration: {k}')
    print(text)
"""
