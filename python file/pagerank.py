# -*- coding: utf-8 -*-

from pygraph.classes.digraph import digraph
import G
import networkx as nx
import time


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
   begin = time.time()
   dg = digraph()

   g = G.init_graph("file_path")
   #g = nx.read_weighted_edgelist("", create_using=nx.DiGraph())

   dg.add_nodes(G.nodes(g))
   for (u, v) in G.edges(g):
       dg.add_edge((u, v))

   pr = PRIterator(dg)
   page_ranks = pr.page_rank()

   #print("The final page rank is\n", page_ranks)

   print("The final page rank is\n", sorted(page_ranks.items(), key=lambda d: d[1]))

   end = time.time()
   print('use time', end - begin)