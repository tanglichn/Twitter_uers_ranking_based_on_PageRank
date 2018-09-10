# -*- coding: utf-8 -*-

from pygraph.classes.digraph import digraph
from collections import Counter
import G
import networkx as nx


class PRIterator:
    __doc__ = '''Calculate the PR value in a graph'''

    def __init__(self, dg):
        self.damping_factor = 0.85  # Damping coefficient, ie α
        self.max_iterations = 100  # The maximum number of iterations
        self.min_delta = 0.00001  # The parameter that determines whether the iteration ends, ie ε
        self.graph = dg

    def page_rank(self):
        #  First change the node without the chain in the figure to the chain for all nodes.
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, node2))

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # Give each node an initial PR value
        damping_value = (1.0 - self.damping_factor) / graph_size  # (1−α)/N part of the formula

        flag = False
        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):  # Traverse all "incident" pages
                    rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node] - rank)  # Absolute value
                page_rank[node] = rank

            print("This is NO.%s iteration" % (i + 1))
            print(page_rank)

            if change < self.min_delta:
                flag = True
                break
        if flag:
            print("finished in %s iterations!" % node)
        else:
            print("finished out of 100 iterations!")
        return page_rank


    #Initialization map
if __name__ == '__main__':
   dg = digraph()
   dg2 = digraph()
   dg3 = digraph()
   dg4 = digraph()

   g = G.init_graph("file_path")
   g2 = G.init_graph("file_path")
   g3 = G.init_graph("file_path")
   g4 = G.init_graph("file_path")

   #g = nx.read_weighted_edgelist("/Users/tangli/Desktop/PageRank_Dissertaion/relations.txt", create_using=nx.DiGraph())
   #g2 = nx.read_weighted_edgelist("/Users/tangli/Desktop/PageRank_Dissertaion/relations_reply.txt", create_using=nx.DiGraph())
   #g3 = nx.read_weighted_edgelist("/Users/tangli/Desktop/PageRank_Dissertaion/relations_retweet.txt", create_using=nx.DiGraph())
   #g4 = nx.read_weighted_edgelist("/Users/tangli/Desktop/PageRank_Dissertaion/relations_mention.txt", create_using=nx.DiGraph())

   dg.add_nodes(G.nodes(g))
   for (u, v) in G.edges(g):
       dg.add_edge((u, v))

   dg2.add_nodes(G.nodes(g2))
   for (u, v) in G.edges(g2):
       dg2.add_edge((u, v))

   dg3.add_nodes(G.nodes(g3))
   for (u, v) in G.edges(g3):
       dg3.add_edge((u, v))

   dg4.add_nodes(G.nodes(g4))
   for (u, v) in G.edges(g4):
       dg4.add_edge((u, v))


   pr = PRIterator(dg)
   page_ranks = pr.page_rank()
   print("The final page rank is\n", page_ranks)

   pr2 = PRIterator(dg2)
   page_ranks2 = pr2.page_rank()
   print("The final page rank is\n", page_ranks2)

   pr3 = PRIterator(dg3)
   page_ranks3 = pr3.page_rank()
   print("The final page rank is\n", page_ranks3)

   pr4 = PRIterator(dg4)
   page_ranks4 = pr4.page_rank()
   print("The final page rank is\n", page_ranks4)

   globalRank = dict(Counter(page_ranks) + Counter(page_ranks2) + Counter(page_ranks3) + Counter(page_ranks4))

   #print("The globalRank is\n", globalRank)

   print("The final Global rank is\n", sorted(globalRank.items(), key=lambda d: d[1]))
