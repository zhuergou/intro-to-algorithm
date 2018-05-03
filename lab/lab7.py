#!/usr/bin/env python3
import numpy as np


def editdistance(seq1, seq2, gp=1, match=0, mismatch=1):
    n = len(seq1)  # seq1 len
    m = len(seq2)  # seq2 len
    print("LEN", n, m)
    M = np.zeros((n + 1, m + 1))  # create n+1 x m+1 DP array
    # TB = np.zeros((n+1, m+1)) #create n+1 x m+1 DP array
    TB = {}  # for trace-back

    moves = ['D', 'V', 'H']  # D, V, H

    # dynamic programming
    # init first row and col
    M[0, 0] = 0
    TB[0, 0] = 'D'
    for j in range(1, m + 1):
        M[0, j] = j * gp
        TB[0, j] = 'H'
    for i in range(1, n + 1):
        M[i, 0] = i * gp
        TB[i, 0] = 'V'

    # fill rest of matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dscore = match
            else:
                dscore = mismatch

            # diagonal (D) move
            D = M[i - 1, j - 1] + dscore
            # horizontal (H) move
            H = M[i, j - 1] + gp
            # vertical (V) move
            V = M[i - 1, j] + gp

            scores = [D, V, H]  # order must match moves
            # get max score
            M[i, j] = min(scores)
            idx = scores.index(M[i, j])

            # store best move
            TB[i, j] = moves[idx]

    # for i in range(n+1):
    #     for j in range(m+1):
    #         print TB[i,j], " ",
    #     print
    # trace back from maxi, maxj
    res1 = []
    res2 = []
    i, j = n, m
    while(i != 0 or j != 0):
        # print i,j, TB[i,j]
        if TB[i, j] == 'D':  # diagonal
            res1.append(seq1[i - 1])
            res2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif TB[i, j] == 'H':  # horizontal
            res1.append('-')
            res2.append(seq2[j - 1])
            j -= 1
        elif TB[i, j] == 'V':  # vertical
            res1.append(seq1[i - 1])
            res2.append('-')
            i -= 1

    res1.reverse()
    res2.reverse()

    a1 = ''.join(res1)
    a2 = ''.join(res2)

    print("edit distance:", M[n, m])

    print("alignment:")
    block = 1000000
    for i in range(0, int(len(a1) / block) + 1):
        lb = i * block
        ub = min((i + 1) * block, len(a1) + 1)
        print(a1[lb:ub])
        print(a2[lb:ub])
        print()


# ################MAIN####################
seq1 = 'CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG'
seq2 = 'CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA'
#seq1 = 'EXPONENTIAL'
#seq2 = 'POLYNOMIAL'
editdistance(seq1, seq2)
