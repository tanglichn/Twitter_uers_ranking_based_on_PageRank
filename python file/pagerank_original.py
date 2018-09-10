import G
import time
import networkx as nx
from pygraph.classes.digraph import digraph


if __name__ == '__main__':
   begin = time.time()
   dg = digraph()

   g = G.init_graph("file_path")

   dg.add_nodes(G.nodes(g))
   for (u, v) in G.edges(g):
       dg.add_edge((u, v))

   pr = nx.pagerank(g, alpha=0.85)
   print('pagerank success')
   result = {}
   for node, value in pr.items():
       result[node] = value
   print("The final page rank is\n", sorted(result.items(), key=lambda d: d[1]))

   end = time.time()
   print('use time', end - begin)