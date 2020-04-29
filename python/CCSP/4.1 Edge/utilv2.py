from dataclasses import dataclass
from utilv1 import Edge, Graph

@dataclass
class WeightedEdge(Edge):
    weight: float

    def reversed(self):
        return WeightedEdge(self.v, self.u, self.weight)

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f"{self.u} {self.weight} -> {self.v}"


class WeightedGraph(Graph):
            
    def add_edge_by_indices(self, u, v, weight):
        edge = WeightedEdge(u, v, weight)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first, second, weight):
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)
        
    def neighbors_for_index_with_weights(self, index):
        distance_tuples = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))

        return distance_tuples


    def __str__(self):
        desc = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
        return desc


def print_weighted_path(wg, wp):
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} {edge.weight} > {wg.vertex_at(edge.v)}")
    print(f"Total Weight: {total_weight(wp)}")


def total_weight(wp):
    return sum([e.weight for e in wp])

if __name__ == "__main__":
    city_graph = WeightedGraph(["Seattle", "San Francisco", "Los Angeles", 
                                "Riverside", "Phoenix", "Chicago", "Boston", 
                                "New York", "Atlanta", "Miami", "Dallas", 
                                "Houston", "Detroit", "Philadelphia", "Washington"])
    
    city_graph.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph.add_edge_by_vertices("Boston", "New York", 190)
    city_graph.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph.add_edge_by_vertices("Philadelphia", "Washington", 123)

    print(city_graph)
