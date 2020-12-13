import networkx as nx
from functions import * # importing all helper functions from functions
from algorithms import prims_algorithm # from algorithms got prims_algorithm

graph_data = open('test-graph/G2.txt', 'r') # reading what's in G1 file 

G = nx.read_weighted_edgelist(graph_data, nodetype= int) # create a graph 

T = initialize_prims(G,3)

print(f'The vertex of  T is V(T) = {V(T)}') # Will print all vertices of the graph 
print('')
print(f'The edge of  T is E(T) = {E(T)}') # Will print all edges of the graph 

#T = prims_algorithm(G, 0)

f = possible_edges(G,T)
e = min_prims_edge(G, T)
temp = cost(G, f[0])
for element in range(0, len(f)):
    if cost(G, f[element]) < temp:
        temp = cost(G,f[element])
        k = element
else:
    k = 0
        
