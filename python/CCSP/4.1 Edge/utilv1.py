from dataclasses import dataclass

@dataclass
class Edge:
    u: int
    v: int

    def reversed(self):
        return Edge(self.v, self.u)

    def __str__(self):
        return f"{self.u} -> {self.v}"


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [[] for _ in vertices]
            
    @property
    def vertex_count(self):
        return len(self._vertices)

    @property
    def edge_count(self):
        return len(self._edges)

    def add_vertex(self, vertex):
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u, v):
        edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first, second):
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indices(u, v)
    
    def vertex_at(self, index):
        return self._vertices[index]

    def index_of(self, vertex):
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index):
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex):
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self,index):
        return self._edges[index]

    def edges_for_vertex(self, vertex):
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self):
        desc = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc


if __name__ == "__main__":
    city_graph = Graph(["Seattle", "San Francisco", "Los Angeles", 
                        "Riverside", "Phoenix", "Chicago", "Boston", 
                        "New York", "Atlanta", "Miami", "Dallas", 
                        "Houston", "Detroit", "Philadelphia", "Washington"])
    
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Boston", "New York")
    city_graph.add_edge_by_vertices("New York", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")

    print(city_graph)
