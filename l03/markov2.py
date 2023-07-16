import numpy as np
import matplotlib.pyplot as plt

T = np.array([[1,1,0,0,1],[1,1,1,0,0],[0,1,1,1,0],[0,0,1,1,1],[1,0,0,1,1]])/3
p=np.random.rand(5)
p=p/np.sum(p)
pfin=np.array([0.2]*5)
ptab=[np.linalg.norm(p-pfin)]
print(p)
#%%
for i in range(100):
    p=T@p
    ptab.append(np.linalg.norm(p-pfin))
    
print(p)

y=range(101)
plt.semilogy(y,ptab)
plt.show()