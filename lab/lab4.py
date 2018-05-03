#!/usr/bin/env python3

import sys
import numpy as np


def select(S, k):
    N = len(S)
    if len(S) == 1:
        return S[0]

    L, V, R = [], [], []

    v = S[np.random.randint(N)]
    for i in range(N):
        if S[i] < v:
            L.append(S[i])
        elif S[i] > v:
            R.append(S[i])
        else:
            V.append(S[i])

    # print("choice", k, v, L, V, R)
    if k <= len(L):
        return select(L, k)
    elif k > len(L) and k <= len(L) + len(V):
        return v
    else:
        return select(R, k - len(L) - len(V))


if __name__ == "__main__":
    N = int(sys.argv[1])  # number of integers to generate
    k = int(sys.argv[2])  # number of integers to generate

    np.random.seed(1)
    S = []
    for i in range(N):
        v = np.random.randint(N)
        S.append(v)

    kth = select(S, k)
    # print("select", kth, sorted(S))
    print("select", kth)
    print("array", S)
    print("sorted array", sorted(S))
