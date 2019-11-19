# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:47:17 2019

@author: Lingxiao Zhou
"""



import networkx as nx
import math as math

#_________________________________________
def fast_gnp_random_graph(n, p, seed=None, directed=False):
    """Returns a $G_{n,p}$ random graph, also known as an Erdős-Rényi graph or
    a binomial graph.
    Parameters:
    n : int
        The number of nodes.
    p : float
        Probability for edge creation.
    """
    G = nx.empty_graph(n)

    if p <= 0 or p >= 1:
        return nx.gnp_random_graph(n, p, seed=seed, directed=directed)

    w = -1
    lp = math.log(1.0 - p)

    if directed:
        G = nx.DiGraph(G)
        # Nodes in graph are from 0,n-1 (start with v as the first node index).
        v = 0
        while v < n:
            lr = math.log(1.0 - seed.random())
            w = w + 1 + int(lr / lp)
            if v == w:  # avoid self loops
                w = w + 1
            while v < n <= w:
                w = w - n
                v = v + 1
                if v == w:  # avoid self loops
                    w = w + 1
            if v < n:
                G.add_edge(v, w)
    else:
        # Nodes in graph are from 0,n-1 (start with v as the second node index).
        v = 1
        while v < n:
            lr = math.log(1.0 - seed.random())
            w = w + 1 + int(lr / lp)
            while w >= v and v < n:
                w = w - v
                v = v + 1
            if v < n:
                G.add_edge(v, w)
    return G

def gnp_random_graph(n, p, seed=None, directed=False):
    """
    Parameters:
    n : int
        The number of nodes.
    p : float
        Probability for edge creation.
    """
    if directed:
        edges = nx.itertools.permutations(range(n), 2)
        G = nx.DiGraph()
    else:
        edges = nx.itertools.combinations(range(n), 2)
        G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)

    for e in edges:
        if seed.random() < p:
            G.add_edge(*e)
    return G


# add some aliases to common names
binomial_graph = gnp_random_graph
erdos_renyi_graph = gnp_random_graph



def dense_gnm_random_graph(n, m, seed=None):
    """
    Parameters:
    n : int
        The number of nodes.
    m : int
        The number of edges.

    """
    mmax = n * (n - 1) / 2
    if m >= mmax:
        G = nx.complete_graph(n)
    else:
        G = nx.empty_graph(n)

    if n == 1 or m >= mmax:
        return G

    u = 0
    v = 1
    t = 0
    k = 0
    while True:
        if seed.randrange(mmax - t) < m - k:
            G.add_edge(u, v)
            k += 1
            if k == m:
                return G
        t += 1
        v += 1
        if v == n:  # go to next row of adjacency matrix
            u += 1
            v = u + 1

def gnm_random_graph(n, m, seed=None, directed=False):
    """
    parameters:
    n : int
        The number of nodes.
    m : int
        The number of edges.
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    G.add_nodes_from(range(n))

    if n == 1:
        return G
    max_edges = n * (n - 1)
    if not directed:
        max_edges /= 2.0
    if m >= max_edges:
        return nx.complete_graph(n, create_using=G)

    nlist = list(G)
    edge_count = 0
    while edge_count < m:
        # generate random edge,u,v
        u = seed.choice(nlist)
        v = seed.choice(nlist)
        if u == v or G.has_edge(u, v):
            continue
        else:
            G.add_edge(u, v)
            edge_count = edge_count + 1
    return G

#_____________________________________
def connected_components(G):
    """Generate connected components.
    Parameters:
        G :  graph
    """
    seen = set()
    for v in G:
        if v not in seen:
            c = set(_plain_bfs(G, v))
            yield c
            seen.update(c)

#_____________________________________

#_____________________________________
def giantc(n,c):
    """
    Give the percent of Giant component.
    
    Parameters:
        n:# of nodes
        c:estimated degree
    """
    mean=0
    for i in range(0,5):
        p=(1.0*c)/(n-1)
        G=nx.fast_gnp_random_graph(n,p)
        components=nx.connected_components(G)
        gene_components=sorted(components, key = len, reverse=True)
        mean=mean+(0.02*len(gene_components[0]))/n
        i=i+1
        print(i)
    return(mean)


#____________________________________________
    

array_c=[]
array_giant=[]
c=0.001
while c<2.5:
    
    array_c.append(c)
    array_giant.append(giantc(1000000,c))
    print(c)
    c=c+0.001
    
    
