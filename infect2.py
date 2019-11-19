# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:10:52 2019

@author: Lingxiao Zhou
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:42:09 2019

@author: Lingxiao Zhou
"""

import networkx as nx
import random
import copy as cp
import numpy as np

def compare(x,y,n):
    for i in range(0,n):
        if x[i] != y[i]:
            return(0)
    return(1)

def randinfect(n,p):
    x=[]
    for i in range(0,n):
        pi=random.uniform(0,1)
        if pi<p:
            x.append(1)
        else:
            x.append(0)
    #print('ini infect')
    return(x)

def infect(G,n,x):
    for i in range(0,n):
        #print(i)
        m=0
        if x[i]==0:
            for j in range(0,n):
                if (G[i,j]==1 and x[j]==1):
                    m=m+1
            if m>=2:
                x[i]=1
                break
    #print('infect +1')
    return(x)
    
def keepinfect(G,n,x):
    y=cp.copy(x)
    x=infect(G,n,x)
    while compare(x,y,n)==0:
        y=cp.copy(x)
        x=infect(G,n,x)
    #print('infect over')
    return(x)

'''
c=5
n=6
psi=1
p=psi*(1.0*c)/(n-1)
G=nx.fast_gnp_random_graph(n,p)
G=nx.adjacency_matrix(G)
print(G)

ini=randinfect(n,0.2)
print(ini)

fin=cp.copy(ini)
ini=infect(G,n,ini)
while((np.array(ini)==np.array(fin)).all()==0):
    fin=cp.copy(ini)
    print(ini)
    ini=infect(G,n,ini)
    print(fin)
    print(ini)
'''

   

c=5
n=100
psi=0.01
array_psi=np.zeros((70,70))
array_s=np.zeros((70,70))
#array_psi=[]
#array_s=[]

for k in range(1,60):
    c=0.1*k
    print(c,'____________________')

    for i in range(0,20):
        psi=0.01+0.05*i
        print('psi',psi)
        mean=0
        for j in range(0,20):
            p=psi*(1.0*c)/(n-1)
            G=nx.fast_gnp_random_graph(n,p)
            G=nx.adjacency_matrix(G)
            ini=randinfect(n,0.1)
            percent=sum(keepinfect(G,n,ini))/n
            mean=mean+(0.05)*percent
    
        array_psi[i][k]=psi
        array_s[i][k]=mean  


'''

while psi<1:
    print(psi)
    mean=0
    
    for i in range(0,20):
        print(i)
        p=psi*(1.0*c)/(n-1)
        G=nx.fast_gnp_random_graph(n,p)
        G=nx.adjacency_matrix(G)
    
        ini=randinfect(n,0.1)
        fin=cp.copy(ini)
        ini=infect(G,n,ini)
        while((np.array(ini)==np.array(fin)).all()==0):
            fin=cp.copy(ini)
            ini=infect(G,n,ini)      
    
        percent=sum(fin)/n
        mean=mean+0.05*percent
    
    array_psi.append(psi)
    array_s.append(percent)
    
    psi=psi+0.05
'''  
'''           
while psi<1:
    print(psi)
    
    p=psi*(1.0*c)/(n-1)
    G=nx.fast_gnp_random_graph(n,p)
    G=nx.adjacency_matrix(G)
    
    ini=randinfect(n,0.1)
    percent=sum(keepinfect(G,n,ini))/n      
    
    array_psi.append(psi)
    array_s.append(percent)
    
    psi=psi+0.05            
'''
        