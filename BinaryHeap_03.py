#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import heapq

data = []

n = int(input())
for i in range(n):
    line = input().strip()
    if " " in line:
        line = [j for j in line.split()]
        line[1] = int(line[1])
        line[1] = -line[1]
        heapq.heappush(data, line[1])
    else:
        print(-heapq.heappop(data))
