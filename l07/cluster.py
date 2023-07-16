import numpy as np
import matplotlib.pyplot as plt

N = 10
lattice=np.random.choice([1,-1],(N,N))
print(lattice)


q=np.random.randint(0,N,2)
print("q=",q)


fliptab = [q.tolist()]
Padd = 0.7

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


visit_n(q)

print(fliptab)


E_mu,E_nu=0,0
for i in fliptab:
    print(i)
    # print(neighbours(i))
    for j in neighbours(np.array(i)):
        if not find(j,fliptab):
            if lattice[i[0]][i[1]] == lattice[j[0]][j[1]]:
                E_mu+=2
            else: E_nu+=2
print("E_mu =",E_mu)
print("E_nu =",E_nu)


cluster=lattice*4
for i in fliptab:
    cluster[i[0]][i[1]] *= 6/4
# print(cluster)
plt.matshow(cluster)
plt.show()

