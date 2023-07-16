import numpy as np
#import random
import matplotlib.pyplot as plt

N = 5
lattice=np.random.choice([1,-1],(N,N))
print(lattice)

def energy(lattice=lattice,N=N):
    E=0
    for i,j in zip(range(N),range(N)):
        E-=(lattice[i][j]*lattice[i][(j+1)%N])
        E-=(lattice[i][j]*lattice[i][j-1])
        E-=(lattice[i][j]*lattice[(i+1)%N][j])
        E-=(lattice[i][j]*lattice[i-1][j])
    return E

beta=0.5
def prob(E=energy(),beta=beta):
    return np.exp(-beta*E)

i,j=np.random.randint(5),np.random.randint(5)

def change():
    return np.random.randint(5),np.random.randint(5)

def energychange(i=i,j=j,lattice=lattice):
    return 2*lattice[i][j]*np.sum([lattice[i][(j+1)%N],lattice[i][j-1],lattice[(i+1)%N][j],lattice[i-1][j]])

def A(ec=energychange(i,j),beta=beta):
    if ec<=0: return 1
    rho=np.exp(-beta*ec)
    return np.min((1,rho))

def accept(i=i,j=j,A=A(energychange(i,j)), lattice = lattice):
    if np.random.random()<A:
        lattice[i][j]*=-1
        accepted = True
    else: accepted = False
    return lattice, accepted

def magnetization(lattice=lattice,N=N):
    return sum(sum(lattice))/N**2



#g=1/(N**2-1)

num = 1000

tab = [energy()]
mtab=[]
for r in range(num*N**2):
    i,j = change()
    lattice, accepted = accept(i,j,A(energychange(i,j)))
    if accepted: tab.append(energychange(i,j)+tab[-1])
    if r%N**2==0: mtab.append(magnetization(lattice))

plt.plot(range(len(mtab)),mtab)
plt.show()