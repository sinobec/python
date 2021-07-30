rects = [[10, 2], [3, 6], [2, 4], [3, 9], [10, 7], [9, 9]]
print(sorted(rects, key = lambda x : x[0]*2 + x[1]*3))