class DisjointSet:
    def __init__(self, vertices: list[str]) -> None:
        self.vertices = vertices
        self.parent = {v: v for v in vertices}
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item: str):
        if self.parent[item] == item:
            return item

        return self.find(self.parent[item])

    def union(self, x: str, y: str):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


vertices = ["A", "B", "C", "D"]

ds = DisjointSet(vertices)
ds.union("A", "B")
