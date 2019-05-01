import numpy as np
import pandas as pd
import itertools
import time
import scipy.optimize as optimize
from data_gen import gen_df 

filename = 'imdb.csv'

df = gen_df(filename)

# Parameters
alphas = np.random.uniform(0,1,3)
betas = [1,2,3]

def u_fun(x1,x2,x3,pars):
        return x1**pars[0]+x2**pars[1]+x3**pars[2]

df_xs = df.iloc[:,13:41]
df_xs['Rating'] = df['imdbRating']
df_xs['Duration'] = df['duration']
df_xs = df_xs[:20]

def obj_fun(df_xs,pars):
        df_xs['Est_rating'] = np.exp(u_fun(df_xs['Action'],df_xs['Drama'],df_xs['Duration'],pars))/(1+np.exp(u_fun(df_xs['Action'],df_xs['Drama'],df_xs['Duration'],pars)))
        df_xs['Difference'] = df_xs['Rating']-df_xs['Est_rating']
        return df_xs['Difference'].sum()

min_fun = lambda a: obj_fun(df_xs,a)

bnds = ((0,1),(0,1),(0,1))

result = optimize.minimize(min_fun,alphas,method='BFGS',bounds=bnds)

print(result.x, alphas)

print(obj_fun(df_xs,alphas),obj_fun(df_xs,result.x))



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
