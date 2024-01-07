from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


#    ["xxxxxxxxxxEx",
#     "x        x x",
#     "x        x x",
#     "x xxxxxxxx x",
#     "x          x",
#     "xSxxxxxxxxxx"]
#
# our base case
# If the direction at which we are pointing rn is valid
# So to check
# 1. If next block width or height is greater than length of maze or
# length of first row is lower, If yes return false -> we are pointing to the edge of the map
# 2. If curr position is a wall, if true return false
# 3. if curr position is the end, return true
dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]

def walk(maze: list[str], wall: str, end: Point, curr: Point, seen: [[bool]], path: list[Point]):
    #  check if it's out of map
    if any([curr.x >= len(maze[0]), curr.x < 0, curr.y >= len(maze), curr.y < 0]):
        return False
    print(curr.y, curr.x)
    if maze[curr.y][curr.x] == wall:
        return False
    if seen[curr.y][curr.x]:
        return False
    if curr.x == end.x and curr.y == end.y:
        path.append(curr)
        return True

    # if not our base case then start recursing
    # pre
    seen[curr.y][curr.x] = True
    path.append(curr)

    # recurse 
    for direction in dirs:
        # if we could find the end, base case would return true
        # so it will propagate to the first walk call
        if (walk(maze, wall, end, 
            Point(curr.x + direction[0], curr.y + direction[1]), seen, path)):
            return True
    # post
    # if we could't find way and it is a dead end
    # we've checked all ours directions and every call will return False 
    # until we go back to that point at our stack where we can find other posible direction
    path.pop()
    return False


def maze_solver(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    path: [Point] = []
    seen = [[False] * len(row) for row in maze] 
    curr = Point(x=start.x, y=start.y)
    walk(maze, wall, end, curr, seen, path)
    return path

maze = ["xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx"]
maze1 = ["xxxxxxxxxx x",
        "x x   x    x",
        "x   x   x xx",
        "x xxxxxxx  x",
        "x xxxxxxx  x",
        "x         xx"]

wall = 'x'
end = Point(x=1, y=5)
start = Point(x=10, y=0) 
path = maze_solver(maze, wall, start, end)
trace = '*'
for point in path:
    row = maze[point.y] 
    new_row = f'{row[:point.x]}{trace}{row[point.x+1:]}'
    maze[point.y] = new_row


