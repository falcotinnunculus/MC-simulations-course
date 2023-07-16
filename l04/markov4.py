#%%
import numpy as np
import matplotlib.pyplot as plt

#T = np.array([[1,1,0,0,1],[1,1,1,0,0],[0,1,1,1,0],[0,0,1,1,1],[1,0,0,1,1]])/3
#T2 = np.transpose([np.add.reduce(T[0:i+1]) for i in range(5)])
g=np.ones((5,5))/5
P=np.random.rand(5)
#P=[1,2,3,4,5]
P=P/np.sum(P)
#%%
A=[[np.min((1,P[n]/P[m])) for m in range(5)] for n in range(5)]

T = g*A
T2 = np.transpose([np.add.reduce(T[0:i+1]) for i in range(5)])
#%%
for i in range(5):
    T[i][i] += 1-T2[i][-1]
    #%%
T2 = np.transpose([np.add.reduce(T[0:i+1]) for i in range(5)])

#%%
for N in [1000000]:
    s = np.random.randint(5)
    stab=[]
    for i in range(N):
        stab.append(s)
        s= np.where(T2[s]>np.random.random())[0][0]
        
    plt.hist(stab,np.arange(0,5,0.5))
    plt.scatter(np.arange(5),P*N,c='#ff7f0e')
    plt.title('n = '+str(N))
    plt.show()
# %%
