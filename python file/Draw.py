import G
import matplotlib.pyplot as plt
import networkx as nx


g = G.init_graph("file_path")
nx.draw(g)
plt.show()