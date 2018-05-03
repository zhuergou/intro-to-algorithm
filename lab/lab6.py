#!/usr/bin/env python3
import heapdict
import sys
from collections import defaultdict

Infinity = 10**10 - 1

G = defaultdict(list)

# read graph and create the edge weight dict
V = {}
W = {}
PAR = defaultdict(int)

with open(sys.argv[1]) as f:  # file name
    for l in f.readlines():
        u, v, w = l.split()
        G[u].append(v)
        PAR[v] += 1
        W[(u, v)] = int(w)
        V[u] = True
        V[v] = True

for v in V.keys():
    if v not in PAR or PAR[v] == 0:
        print("source", v)

s = sys.argv[2]  # source node

# for u in G:
#     for v in G[u]:
#         print (u,v, W[(u,v)])


# disjkstra's algorithm
dist = heapdict.heapdict()
prev = {}
for u in V.keys():
    dist[u] = Infinity
    # print ("adding", u)
    prev[u] = None

dist[s] = 0
SPL = {}
while dist:
    u, dist_u = dist.popitem()
    SPL[u] = dist_u
    # print ("popped", u, dist_u, dist)
    for v in G[u]:
        if v in dist and dist[v] > dist_u + W[(u, v)]:
            # print ("check", v, dist[v], W[(u,v)])
            dist[v] = dist_u + W[(u, v)]
            prev[v] = u

# for u in SPL:
#     print("prev", u, prev[u])
for u in sorted(SPL):
    x = u
    path = []
    while x:
        path.append(x)
        x = prev[x]
    path.reverse()
    print(u, SPL[u], path)
