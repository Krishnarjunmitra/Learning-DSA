"""
Graph Data Structure: Theory and Implementation (Adjacency List)
"""

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)  # For undirected graph

    def get_neighbors(self, vertex):
        return self.adj_list.get(vertex, [])

'''
Use Cases:
- Social networks (users as nodes, friendships as edges)
- Web page links (web pages as nodes, hyperlinks as edges)
- Network routing (routers as nodes, connections as edges)
- Course prerequisites (courses as nodes, dependencies as edges)
'''
