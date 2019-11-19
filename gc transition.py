# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:21:00 2019

@author: Lingxiao Zhou
"""


from networkx.utils import powerlaw_sequence
import networkx as nx
import networkx.utils as utils

def giantc(n,c):
    mean=0
    for i in range(0,10):
        p=(1.0*c)/n
        G=nx.fast_gnp_random_graph(n,p)
        components=nx.connected_components(G)
        gene_components=sorted(components, key = len, reverse=True)
        mean=mean+(0.1*len(gene_components[0]))/n
        i=i+1
        print(i)
    return(mean)

def pogiantc(n,c):
    mean=0
    for i in range(0,1):
        z=utils.create_degree_sequence(100,powerlaw_sequence)
        print(z)
        G=nx.configuration_model(z)
        components=nx.connected_components(G)
        gene_components=sorted(components, key = len, reverse=True)
        mean=mean+(1.0*len(gene_components[0]))/n
        i=i+1
        print(i)
    return(mean)

array_c=[]
array_giant=[]
c=0.01
while c<2.5:
    
    array_c.append(c)
    array_giant.append(giantc(100,c))
    print(c)
    c=c+0.01
    
    
