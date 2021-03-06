from util import Maze, MazeLocation, Cell, Node, node_to_path



def dfs(initial, goal_test, successors):
    frontier = []
    frontier.append(Node(initial, None))
    explored = {initial}

    while frontier:
        current_node = frontier.pop()
        current_state = current_node.state
        
        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.append(Node(child, current_node))
        
    return None


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