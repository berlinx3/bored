from heapq import heappop, heappush
from util import Maze, MazeLocation, Cell, Node, node_to_path

def astar(initial, goal_test, successors, heuristic):
    frontier = []
    heappush(frontier, Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}

    while frontier:
        current_node = heappop(frontier)
        current_state = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            new_cost = current_node.cost + 1

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                heappush(frontier,Node(child, current_node, new_cost, heuristic(child)))
        
    return None


def manhattan_distance(goal):
    def distance(m1):
        xdist = abs(m1.column - goal.column)
        ydist = abs(m1.row - goal.row)
        return (xdist - ydist)
    return distance

    
if __name__ == "__main__":
    m = Maze()
    print(m)

    distance = manhattan_distance(m.goal)

    solution1 = astar(m.start, m.goal_test, m.successors, distance)

    if solution1 is None:
        print("No solution found using depth-first search!")
    else:
        path1 = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)