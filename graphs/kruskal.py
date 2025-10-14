from disjointSet import DisjointSet
from typing import Optional


class KrusKalMST:
    def __init__(self, vertices: int = 0) -> None:
        self.v_count = vertices
        self.graph: list[tuple[str, str, int]] = []
        self.nodes = []
        self.max_weight = 0
        self.mst: list[tuple[str, str, int]] = []

    def addEdge(self, s: str, d: str, w: int):
        if w > self.max_weight:
            self.max_weight = w
        self.graph.append((s, d, w))

    def addNode(self, node):
        self.nodes.append(node)

    def printSoln(self, s: str, d: str, weight: int):
        for s, d, weight in self.mst:
            print(f"{s} - {d}: {weight}")

    def run_kruskal(self):
        vertex, edge = 0, 0
        ds = DisjointSet(self.nodes)

        # sort the graph based on wieght
        graph = sorted(self.graph, key=lambda item: item[2])

        while edge < self.v_count - 1:
            s, d, weight = graph[vertex]
            vertex += 1
            x = ds.find(s)
            y = ds.find(d)
            # if disjoined
            if x != y:
                edge += 1
                self.mst.append((s, d, weight))
                # may x
                ds.union(x, y)

        self.printSoln(s, d, weight)

    # O(V^3) for Time and O(V) for space
    def run_prims(self):
        edgeIndex = 0
        visited: list[Optional[str]] = [None] * self.v_count
        visited[3] = self.nodes[3]

        while edgeIndex < self.v_count - 1:
            min = self.max_weight
            selected_node: Optional[tuple[str, str, int]] = None
            selected_node_index = -1
            for i in range(self.v_count):
                # for each visited node, check for,
                # adajacent node with lowest weight
                if visited[i] != None:
                    possible_nodes = [
                        n
                        for n in self.graph
                        if n[0] == self.nodes[i] and n[1] not in visited
                    ]
                    for n in possible_nodes:
                        if min > n[2]:
                            selected_node_index = self.nodes.index(n[1])
                            selected_node = n
                            min = n[2]

            if selected_node != None:
                visited[selected_node_index] = self.nodes[selected_node_index]
                self.mst.append(selected_node)
                edgeIndex += 1

        self.printSoln(*self.mst[0])


kmst = KrusKalMST(5)
#
#     A -------B
#  15/|   5  / |
#   / |     /  |
# E 13|  10/   |8
#   \ |   /    |
# 20 \| /  6   |
#     C -------D
kmst.addNode("A")
kmst.addNode("B")
kmst.addNode("C")
kmst.addNode("D")
kmst.addNode("E")
kmst.addEdge("A", "B", 5)
kmst.addEdge("A", "C", 13)
kmst.addEdge("A", "E", 15)
kmst.addEdge("B", "A", 5)
kmst.addEdge("B", "D", 8)
kmst.addEdge("B", "C", 10)
kmst.addEdge("C", "E", 20)
kmst.addEdge("C", "A", 13)
kmst.addEdge("C", "B", 10)
kmst.addEdge("C", "D", 6)
kmst.addEdge("D", "C", 6)
kmst.addEdge("D", "B", 8)
kmst.addEdge("E", "A", 15)
kmst.addEdge("E", "C", 20)

# kmst.run_kruskal()
kmst.run_prims()
