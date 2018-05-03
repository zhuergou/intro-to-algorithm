#!/usr/bin/env python3
import sys
from collections import defaultdict


def dfs_number(G, v):
    global dfs
    global visited
    global post

    visited[v] = True
    dfs += 1
    interval[v].append(dfs)
    for x in G[v]:
        if not visited[x]:
            dfs_number(G, x)
    dfs += 1
    interval[v].append(dfs)
    post.append(v)


def connected_component(G, v, CC):
    global visited

    visited[v] = True
    CC.append(v)
    for x in G[v]:
        if not visited[x]:
            connected_component(G, x, CC)


# MAIN
G = defaultdict(list)
GR = defaultdict(list)

# read graph and create the reverse graph
V = {}
with open(sys.argv[1]) as f:  # file name
    for l in f.readlines():
        u, v = l.split()
        G[u].append(v)
        GR[v].append(u)
        V[u] = True
        V[v] = True
# sys.setrecursionlimit(len(V.keys()))

visited = defaultdict(bool)
for v in V:
    visited[v] = False

# print("V", V)
post = []
interval = defaultdict(list)
# for v in V:
#     print v, GR[v], interval[v]
dfs = 0
for v in V:
    if not visited[v]:
        dfs_number(GR, v)


for v in V:
    visited[v] = False

# print("len post", post)
while post:
    v = post.pop()
    if not visited[v]:
        CC = []
        connected_component(G, v, CC)
        if len(CC) >= 1:
            # print("CC", v, len(CC), CC)
            for x in CC:
                print(x, " ", end='')
            print()
