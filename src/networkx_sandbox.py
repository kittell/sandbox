'''
Created on Mar 16, 2020

@author: kirk@kirkkittell.com
'''

# https://stackoverflow.com/questions/20133479/how-to-draw-directed-graphs-using-networkx-in-python
# https://networkx.github.io/

import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([('D', 'B'), ('D', 'C'), ('D', 'A'), ('D', 'D')])
nx.draw_networkx(G, arrows=True)

plt.show()