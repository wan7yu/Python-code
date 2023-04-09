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


# 栈方法实现，非最短路径
def maze_path(x1, y1, x2, y2):
    stack = []
    # 将起点入栈
    stack.append((x1, y1))
    maze[x1][y1] = 2
    while (len(stack) > 0):
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print(p)
            return True
        # x,y 四个方向 x-1,y; x+1,y; x,y-1; x,y+1;
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                # 2表示已经走过
                maze[nextNode[0]][nextNode[1]] = 2
                break
        # 如果4个方向都不能走就回退一格
        else:
            stack.pop()
    else:
        print("没有路可到终点")
        return False


maze_path(1, 1, 8, 8)
