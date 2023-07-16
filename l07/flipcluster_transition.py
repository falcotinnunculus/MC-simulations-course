import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)
from matplotlib.animation import FuncAnimation
from time import time

N = 32
lattice=np.random.choice([1,-1],(N,N))
# print(lattice)

beta = 0.5
Padd = 1-np.exp(-2*beta)

def neighbours(q):
    return (q+[[0,1],[0,-1],[1,0],[-1,0]])%N

def find(i,fliptab):
    try:
        if fliptab.index(i.tolist()) > -1:
            return True
    except ValueError:
        return False

def visit_n(q):
    for i in neighbours(q):
        # print("visiting",i)
        # print(lattice[q[0]][q[1]], "==", lattice[i[0]][i[1]])
        # print(find(i,fliptab))
        if lattice[q[0]][q[1]] == lattice[i[0]][i[1]] and not find(i,fliptab):
            if Padd>np.random.random():
                fliptab.append(i.tolist())
                # print(i)
                visit_n(i)

def magnetization(lattice=lattice,N=N):
    return abs(sum(sum(lattice))/N**2)

btab=[]
timetab=[]
errtab=[]
for beta in (ran:=np.arange(0,1,0.04)):
    start = time()
    mtab=[]
    ctab=[]
    lattice=np.random.choice([1,-1],(N,N))
    Padd = 1-np.exp(-2*beta)
    T = 200
    for i in range(T):
        q=np.random.randint(0,N,2)
        # print("q=",q)
        fliptab = [q.tolist()]
        visit_n(q)
        for i in fliptab:
            lattice[i[0]][i[1]] *= -1
        # print(lattice)
        mtab.append(magnetization(lattice,N))
    btab.append(np.mean(mtab[-30:].copy()))
    errtab.append(np.std(mtab[-30:].copy()))
    print(beta, end:=time()-start)
    timetab.append(end)
    # print(mtab)

fig,ax = plt.subplots()
ax2=ax.twinx()
ax.errorbar(ran,btab,yerr=errtab,color="red")
ax.set_ylabel("magnetization",color="red")
ax2.plot(ran,timetab,color="blue")
ax2.set_ylabel("runtime [s]",color="blue")
plt.show()
