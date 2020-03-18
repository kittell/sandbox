'''
Created on Mar 16, 2020

@author: kirk@kirkkittell.com
'''

# Documentation: https://networkx.github.io/documentation/stable/

import matplotlib.pyplot as plt
import networkx as nx

# (1) Create a graph

G = nx.DiGraph()
G.add_edges_from([('D', 'B'), ('D', 'C'), ('D', 'A'), ('D', 'D')])
nx.draw_networkx(G, arrows=True)

plt.show()