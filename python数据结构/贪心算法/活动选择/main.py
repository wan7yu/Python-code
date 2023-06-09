"""
派对要举办一些活动，怎么样设计活动的顺序能让
出演的活动最多而时间又不冲突呢
ac      1   2   3   4   5   6   7   8   9   10  11
start:  1   3   0   5   3   5   6   8   8   2   12  
end:    4   5   6   7   9   9   10  11  12  14  16
"""
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
              (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# 保证活动是按结束时间升序排序
activities.sort(key=lambda x: x[1])


def activity_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] > res[-1][1]:
            res.append(a[i])
    return res


print(activity_selection(activities))
