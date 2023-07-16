#%%
import numpy as np
import matplotlib.pyplot as plt

#T = np.array([[1,1,0,0,1],[1,1,1,0,0],[0,1,1,1,0],[0,0,1,1,1],[1,0,0,1,1]])/3
#T2 = np.transpose([np.add.reduce(T[0:i+1]) for i in range(5)])
g=np.ones((2,2))/2
#P=np.random.rand(5)
P=[1,0.1]
P=P/np.sum(P)
#%%
A=[[np.min((1,P[n]/P[m])) for m in range(2)] for n in range(2)]

# T = g*A
# T2 = np.transpose([np.add.reduce(T[0:i+1]) for i in range(2)])
# #%%
# for i in range(2):
#     T[i][i] += 1-T2[i][-1]
#     #%%

T=np.array([[0.9,0.1],[0.1,0.9]])
T2 = np.transpose([np.add.reduce(T[0:i+1]) for i in range(2)])

#%%
for N in [1000]:
    s = np.random.randint(2)
    stab=[]
    for i in range(N):
        stab.append(s)
        s= np.where(T2[s]>np.random.random())[0][0]
    
    plt.scatter(range(N),stab)
    plt.show()

    C=[]
    for t in range(0,int(N/2)):
        sisit = np.array(stab[0:N-t])*np.array(stab[t:N])
        C.append(1/(N-t)*np.sum(sisit) - (1/N*np.sum(stab))**2)
        # if t%1000==0: print(t)

    plt.plot(range(0,int(N/2)),C)
    #plt.semilogy()
    plt.show()


# %%
