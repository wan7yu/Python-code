from collections import deque


# 定义迷宫，1为墙，0为路
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
# 四个方向
dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y-1),
    lambda x, y: (x, y+1)
]


def print_path(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    # 起点
    realpath.append(curNode[0:2])
    realpath.reverse()
    print("最短路径为:")
    for node in realpath:
        print(node)


# 队列方法，为最短路径
def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 终点
            print_path(path)
            return True
        # x,y 四个方向 x-1,y; x+1,y; x,y-1; x,y+1;
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                # 后续节点进队，记录哪个节点带它来的
                queue.append((nextNode[0], nextNode[1], len(path)-1))
                # 2表示已经走过
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        print("没有路可到终点")
        return False


maze_path_queue(1, 1, 8, 8)
