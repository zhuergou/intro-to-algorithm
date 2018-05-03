#!/usr/bin/env python3
import random
import sys

Carmichael = [
    561,
    1105,
    1729,
    2465,
    2821,
    6601,
    8911,
    10585,
    15841,
    29341,
    41041,
    46657,
    52633,
    62745,
    63973,
    75361,
    101101,
    115921,
    126217,
    162401,
    172081,
    188461,
    252601,
    278545,
    294409,
    314821,
    334153,
    340561,
    399001,
    410041,
    449065,
    488881]


def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, y >> 1, N)
    if y & 1 == 0:  # even
        return (z**2) % N
    else:
        return (x * z**2) % N


def run(N, k, print_prob=False):
    prime = True
    false_cnt = 0
    for i in range(k):
        a = random.randint(2, N - 1)
        res = modexp(a, N - 1, N)
        # print("test", i, a, res)
        if res != 1:
            prime = False
            false_cnt += 1

    if print_prob:
        print(N, "is prime", prime, "prob", false_cnt / k)
    else:
        print(N, "is prime", prime)


if __name__ == "__main__":
    N = int(sys.argv[1])  # test primality
    k = int(sys.argv[2])  # how many repeats
    run(N, k)

    for N in Carmichael:
        run(N, k, True)
