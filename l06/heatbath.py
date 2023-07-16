import numpy as np
import matplotlib.pyplot as plt

N = 5
lattice=np.random.choice([1,-1],(N,N))
print(lattice)

# def energy(lattice=lattice,N=N):
#     E=0
#     for i in range(N):
#         for j in range(N):
#             E-=(lattice[i][j]*lattice[i][(j+1)%N])
#             E-=(lattice[i][j]*lattice[i][j-1])
#             E-=(lattice[i][j]*lattice[(i+1)%N][j])
#             E-=(lattice[i][j]*lattice[i-1][j])
#     return E

q=np.random.randint(0,N,2)
print(q)

beta=0.01
J=1

def energychange(i,j,lattice=lattice):
    return np.sum([lattice[i][(j+1)%N],lattice[i][j-1],lattice[(i+1)%N][j],lattice[i-1][j]])

def prob(q):
    ec=energychange(*q)
    return np.exp(beta*J*ec)/(np.exp(beta*J*ec)+np.exp(-beta*J*ec))
print(prob(q))

def swap(q,lattice):
    if prob(q)>np.random.random():
        lattice[q[0]][q[1]]=1
    else:
        lattice[q[0]][q[1]]=-1
    return lattice

def magnetization(lattice=lattice,N=N):
    return abs(sum(sum(lattice))/N**2)

# l=0
# mtab=[]
# for c in range(10000):
#     for i in range(N):
#         for j in range(N):
#             lattice=swap((i,j),lattice)
#             l+=1
#     if c%N**2==0: mtab.append(magnetization(lattice))

# print(lattice)

btab=[]
for beta in np.arange(0,1,0.04):
    print(beta)
    l=0
    mtab=[]
    for c in range(2000):
        for i in range(N):
            for j in range(N):
                lattice=swap((i,j),lattice)
                l+=1
        if c%N**2==0: mtab.append(magnetization(lattice))
    btab.append(np.mean(mtab[10:]))

plt.plot(np.arange(0,1,0.04),btab)
plt.show()