import networkx as nx
import os


def init_graph(file_path):
    graph = nx.DiGraph()  # Initialize an empty map
    if os.path.isfile(file_path) == False:
        open(file_path, "w")
    file = open(file_path, "r")
    try:
        lines = file.readlines()
    except:
        file.close
    file.close
    for line in lines:
        tail, head = line.split(' ')
        graph.add_edge(head.strip(), tail.strip())  # Add the relationship pair to the diagram
    return graph


def nodes(self):
    return self.nodes()


def number_of_edges(self):
    return self.number_of_edges()


def edges(self):
    return self.edges()



