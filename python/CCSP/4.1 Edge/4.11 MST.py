from heapq import heappop, heappush
from utilv2 import WeightedEdge, WeightedGraph, print_weighted_path



"""
Minimum Spanning tree using Jarnik's algorithm
"""
def mst(wg, start = 0):
    if start > (wg.vertex_count - 1) or start < 0:
        return None
    
    result = []
    pq = []
    visited = [False] * wg.vertex_count

    def visit(index):
        visited[index] = True
        for edge in wg.edges_for_index(index):
            if not visited[edge.v]:
                heappush(pq, edge)

    visit(start)

    while pq:
        edge = heappop(pq)

        if visited[edge.v]:
            continue
        result.append(edge)
        visit(edge.v)
    return result






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

    result = mst(city_graph)

    if result is None:
        print("No solution found!")
    else:
        print_weighted_path(city_graph, result)