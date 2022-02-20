from collections import deque


def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    def searchRoom(row, col):
        # Skip if the searching room is not in the grid
        # or has been visited or is a gate or is a wall
        if (
            row < 0 or row == len_row or col < 0 or col == len_col or
            (row, col) in visited or rooms[row][col] == -1
        ):
            return
        queue.append([row, col])
        visited.add((row, col))

    # Save visited room to not be re-visited
    visited = set()
    # dequeue is preferred over a list in the cases where
    # we need quicker append and pop operations from both
    # the ends of the container, as deque provides an O(1) time complexity
    queue = deque()
    len_row, len_col = len(rooms), len(rooms[0])

    # Produce queue that contains only gates to perform BFS on
    for row in range(len_row):
        for col in range(len_col):
            if rooms[row][col] == 0:
                queue.append([row, col])
                visited.add((row, col))

    dist = 0
    # Go through the actual gates
    while len(queue) > 0:
        # Loop through each BFS steps away from the gate
        for i in range(len(queue)):
            row, col = queue.popleft()
            rooms[row][col] = dist
            searchRoom(row, col+1)
            searchRoom(row, col-1)
            searchRoom(row+1, col)
            searchRoom(row-1, col)
        dist += 1


rooms = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
]
wallsAndGates(rooms)
