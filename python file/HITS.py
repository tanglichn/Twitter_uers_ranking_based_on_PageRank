
from pygraph.classes.digraph import digraph
import G
import time
from numpy import *
set_printoptions(threshold=NaN)


class HITSIterator:
    __doc__ = '''Calculate the hub, authority value in a graph'''

    def __init__(self, dg):
        self.max_iterations = 100  # The maximum number of iterations
        self.min_delta = 0.0001  # Determine the parameters of whether the iteration ends
        self.graph = dg

        self.hub = {}
        self.authority = {}
        for node in self.graph.nodes():
            self.hub[node] = 1
            self.authority[node] = 1

    def hits(self):
        """
        Calculate the hub, authority value of each page
        :return:
        """
        begin = time.time()
        if not self.graph:
            return

        flag = False
        for i in range(self.max_iterations):
            change = 0.0  # Record the change value of each round
            norm = 0  # Standardization coefficient
            tmp = {}
            # Calculate the authority value for each page
            tmp = self.authority.copy()
            for node in self.graph.nodes():
                self.authority[node] = 0
                for incident_page in self.graph.incidents(node):  # Traverse all "incident" pages
                    self.authority[node] += self.hub[incident_page]
                norm += pow(self.authority[node], 2)
            # standardization
            norm = math.sqrt(norm)
            for node in self.graph.nodes():
                self.authority[node] /= norm
                change += abs(tmp[node] - self.authority[node])

            # Calculate the hub value of each page
            norm = 0
            tmp = self.hub.copy()
            for node in self.graph.nodes():
                self.hub[node] = 0
                for neighbor_page in self.graph.neighbors(node):  # Traverse all "out of the way" pages
                    self.hub[node] += self.authority[neighbor_page]
                norm += pow(self.hub[node], 2)
            # standardization
            norm = math.sqrt(norm)
            for node in self.graph.nodes():
                self.hub[node] /= norm
                change += abs(tmp[node] - self.hub[node])

            print("This is NO.%s iteration" % (i + 1))
            #print("authority", sorted(self.authority.items(), key=lambda d: d[1], reverse=True))
            #print("hub", sorted(self.hub.items(), key=lambda d: d[1], reverse=True))

            if change < self.min_delta:
                flag = True
                break
        if flag:
            print("finished in %s iterations!" % (i + 1))
        else:
            print("finished out of 100 iterations!")

        print("authority", sorted(self.authority.items(), key=lambda d: d[1]))
        print("hub", sorted(self.hub.items(), key=lambda d: d[1]))
        print("The best authority page: ", max(self.authority.items(), key=lambda x: x[1]))
        print("The best hub page: ", max(self.hub.items(), key=lambda x: x[1]))
        end = time.time()
        print('use time', end - begin)


if __name__ == '__main__':
    dg = digraph()

    g = G.init_graph("file_path")

    dg.add_nodes(G.nodes(g))
    for (u, v) in G.edges(g):
        dg.add_edge((u, v))

    hits = HITSIterator(dg)
    hits.hits()
