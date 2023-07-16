import numpy as np
#import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import time

N = 5
lattice=np.random.uniform(-np.pi,np.pi,(N,N))
# print(lattice)

def energy(lattice=lattice,N=N):
    E=0
    for i,j in zip(range(N),range(N)):
        E-=np.cos(lattice[i][j]-lattice[i][(j+1)%N])
        E-=np.cos(lattice[i][j]-lattice[i][j-1])
        E-=np.cos(lattice[i][j]-lattice[(i+1)%N][j])
        E-=np.cos(lattice[i][j]-lattice[i-1][j])
    return E

beta=0.2
# def prob(E=energy(),beta=beta):
#     return np.exp(-beta*E)

i,j=np.random.randint(N),np.random.randint(N)

def change():
    return np.random.randint(N),np.random.randint(N)

def newangle(oldangle, sigma=0.1):
    na = np.random.normal(oldangle,sigma)
    if na > np.pi: return na - 2*np.pi
    if na < -np.pi: return na + 2*np.pi
    return na

def energychange(i,j,angle,lattice=lattice):
    # return 2*lattice[i][j]*np.sum([lattice[i][(j+1)%N],lattice[i][j-1],lattice[(i+1)%N][j],lattice[i-1][j]])
    ec=0
    ec-=np.cos(angle-lattice[i][(j+1)%N])-np.cos(lattice[i][j]-lattice[i][(j+1)%N])
    ec-=np.cos(angle-lattice[i][j-1])-np.cos(lattice[i][j]-lattice[i][j-1])
    ec-=np.cos(angle-lattice[(i+1)%N][j])-np.cos(lattice[i][j]-lattice[(i+1)%N][j])
    ec-=np.cos(angle-lattice[i-1][j])-np.cos(lattice[i][j]-lattice[i-1][j])
    return ec

def A(ec,beta=beta):
    if ec<=0: return 1
    rho=np.exp(-beta*ec)
    return np.min((1,rho))

def accept(i,j,A, angle, lattice = lattice):
    if np.random.random()<A:
        lattice[i][j]=angle
        accepted = True
    else: accepted = False
    return lattice, accepted

def magnetization(lattice=lattice,N=N):
    m = lattice-lattice[0][0]
    np.where(m<-np.pi,2*np.pi+m,m)
    np.where(m>np.pi,-2*np.pi+m,m)
    x=np.cos(m)
    y=np.sin(m)
    return np.sqrt(np.sum(np.sum(x))**2+np.sum(np.sum(y))**2)/N**2



#g=1/(N**2-1)

# num = 1000

# tab = [energy()]
# mtab=[]
# ctab=[]
# for r in range(T:=num*N**2):
#     i,j = change()
#     angle=newangle(lattice[i][j])
#     lattice, accepted = accept(i,j,A(energychange(i,j,angle)),angle)
#     if accepted: tab.append(energychange(i,j,angle)+tab[-1])
#     if r%N**2==0: mtab.append(magnetization(lattice))
#     ctab.append(lattice.copy())


btab=[]
timetab=[]
errtab=[]
for beta in (ran:=np.concatenate([np.arange(0,1,0.04),np.arange(1,10,0.4),np.arange(10,100,4)])):
    start=time()
    num = 1000
    tab = [energy()]
    mtab=[]
    ctab=[]

    for r in range(T:=num*N**2):
        i,j = change()
        angle=newangle(lattice[i][j])
        lattice, accepted = accept(i,j,A(energychange(i,j,angle),beta),angle)
        if accepted: tab.append(energychange(i,j,angle)+tab[-1])
        if r%N**2==0: mtab.append(magnetization(lattice))
        if beta == 98: ctab.append(lattice-lattice[0][0])

    btab.append(np.mean(mtab[-num*N:].copy()))
    errtab.append(np.std(mtab[-num*N:].copy()))
    print(beta, end:=time()-start, mtab[-1], np.mean(mtab[-num*N:]), np.std(mtab[-num*N:]))
    timetab.append(end)
    # print(mtab)

# speed=50
# fig,ax=plt.subplots()
# def animate(i):
#     ax.clear()
#     ax.matshow(ctab[i*speed],vmin=-np.pi,vmax=np.pi)
#     ax.set_title(magnetization(ctab[i*speed]))

# ani = FuncAnimation(fig, animate, frames=int(T/speed), interval=1, repeat=False)
# plt.show()

fig,ax = plt.subplots()
ax2=ax.twinx()
ax.errorbar(ran,btab,yerr=errtab,color="red")
ax.set_ylabel("magnetization",color="red")
ax.set_xlabel("beta",color="red")
ax.semilogx()
# ax2.plot(ran,timetab,color="blue")
# ax2.set_ylabel("runtime [s]",color="blue")
plt.show()

