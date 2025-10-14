from typing import Optional


class Graph:
    def __init__(self, gdict: dict[str, list[str]] = {}) -> None:
        self.gdict = gdict

    def add_edge(self, vertex: str, edge: str):
        if vertex in self.gdict and edge in self.gdict:
            self.gdict[vertex].append(edge)

    def add_vertex(self, vertex: str):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    def print_graph(self):
        for vertex in self.gdict:
            print(vertex, " : ", self.gdict[vertex])

    def remove_edge(self, vertex: str, edge: str):
        if vertex in self.gdict and edge in self.gdict:
            self.gdict[vertex].remove(edge)

    def remove_vertex(self, vertex: str):
        if vertex in self.gdict:
            for curr_vertex in self.gdict:
                if vertex in self.gdict[curr_vertex]:
                    self.gdict[curr_vertex].remove(vertex)
            del self.gdict[vertex]


defaultGraph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "E", "F"],
    "E": ["D", "F"],
    "F": ["D", "E"],
}

g = Graph(defaultGraph)
g.add_edge("E", "C")
g.gdict.get("E", [])
g.remove_edge("E", "D")
g.remove_vertex("F")
g.print_graph()
