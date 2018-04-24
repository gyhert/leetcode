import collections
n = 3
edges = [[0,1,100], [1,2,100], [0,2,500]]
src = 0
dst = 2
k = 0
f = collections.defaultdict(dict)
for a, b, p in edges:
    f[a][b] = p
heap = [(0, src, k + 1)]
print(f[0][1])
"""
while heap:
    p, i, k = heap.pop(heap)
    if i == dst:
        print(p)
    if k > 0:
        for j in f[i]:
            heap.heappush(heap, (p + f[i][j], j, k -1))
print(-1)
"""