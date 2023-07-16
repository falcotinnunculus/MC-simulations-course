import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)
from matplotlib.animation import FuncAnimation

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

mtab=[]
ctab=[]
T = 200
for i in range(T):
    q=np.random.randint(0,N,2)
    # print("q=",q)
    fliptab = [q.tolist()]
    visit_n(q)

    cluster=lattice.copy()
    cluster*=4
    ctab.append(cluster.copy())
    for j in fliptab:
        cluster[j[0]][j[1]] *= 6/4
    ctab.append(cluster.copy())

    for i in fliptab:
        lattice[i[0]][i[1]] *= -1
    # print(lattice)
    mtab.append(magnetization(lattice,N))
print(mtab)

# print(fliptab)


# E_mu,E_nu=0,0
# for i in fliptab:
#     print(i)
#     # print(neighbours(i))
#     for j in neighbours(np.array(i)):
#         if not find(j,fliptab):
#             if lattice[i[0]][i[1]] == lattice[j[0]][j[1]]:
#                 E_mu+=2
#             else: E_nu+=2
# print("E_mu =",E_mu)
# print("E_nu =",E_nu)


# cluster=lattice*4
# for i in fliptab:
#     cluster[i[0]][i[1]] *= 6/4
# print(cluster)
# plt.matshow(cluster)
# plt.show()

fig,ax=plt.subplots()
def animate(i):
    ax.clear()
    ax.matshow(ctab[i],vmin=-6,vmax=6)
    if not i%2: ax.set_title(str(int(i/2))+" lattice")
    else: ax.set_title(str(int((i-1)/2))+" cluster")

ani = FuncAnimation(fig, animate, frames=2*T, interval=100, repeat=False)
plt.show()
