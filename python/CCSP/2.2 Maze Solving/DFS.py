from util import Maze, MazeLocation, Cell

class Node():
    def __init__(self, state, parent, cost = 0.0, heuristic = 0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def node_to_path(node):
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    
    path.reverse()
    return path


def dfs(initial, goal_test, successors):
    frontier = []
    frontier.append(Node(initial, None))
    explored = {initial}

    while len(frontier) > 0:
        current_node = frontier.pop()
        current_state = current_node.state
        
        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.append(Node(child, current_node))
        
    return Node


if __name__ == "__main__":
    m = Maze()
    print(m)

    solution1 = dfs(m.start, m.goal_test, m.successors)

    if solution1 is None:
        print("No solution found using depth-first search!")
    else:
        path1 = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)