#!/usr/bin/env python3
import sys
import timeit
import random


class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


def multiply_naive(x, y):
    '''high school multiplication function, sec 1.1.2  in DPV'''
    if y == 0:
        return 0
    sumv = 0
    shift = 0
    z = y
    while z > 0:
        if z & 1 != 0:
            sumv += (x << shift)
        shift += 1
        z = z >> 1

    return sumv


def multiply(x, y):
    '''recursive multiplication function, alg 1.1 in DPV'''
    if y == 0:
        return 0
    z = multiply(x, y >> 1)  # use bit shift to right to divide by 2
    if y & 1 == 0:  # y is even
        return 2 * z
    else:
        return x + 2 * z


def multiply_nr(x, y):
    '''non-recursive 1.1'''
    res = 0
    yl = y.bit_length()
    eo_check = 1 << yl
    for i in range(yl + 1):
        if y & eo_check == 0:  # even
            res = res << 1  # 2*res
        else:
            res = (res << 1) + x  # 2*res+x
        eo_check = eo_check >> 1
    return res


# @memoize
# def multiply_dc(x, y):
#     n = max(x.bit_length(), y.bit_length())
#     if n == 1:
#         return x * y
#     n2 = n >> 1
#     xl = x >> n2  # shift right by n/2 to get xl
#     xr = x - (xl << n2)
#     yl = y >> n2  # shift right by n/2 to get yl
#     yr = y - (yl << n2)
#     P1 = multiply_dc(xl, yl)
#     P2 = multiply_dc(xr, yr)
#     P3 = multiply_dc(xl + xr, yl + yr)
#     z = P3 - P2 - P1
#     return (P1 << (2 * n2)) + (z << n2) + P2


@memoize
def multiply_dc(x, y, n):
    '''divide-conquer multiplication function, alg 2.1 in DPV'''
    '''n is number of bits; assumed to be even'''
    if n == 1:
        return x * y

    n2 = n >> 1
    n1 = n - n2
    xl = x >> n2  # shift right by n/2 to get xl
    xr = x - (xl << n2)
    yl = y >> n2  # shift right by n/2 to get yl
    yr = y - (yl << n2)

    P1 = multiply_dc(xl, yl, n1)
    P2 = multiply_dc(xr, yr, n2)
    P3 = multiply_dc(xl + xr, yl + yr, n1)
    z = P3 - P2 - P1
    return (P1 << (2 * n2)) + (z << n2) + P2


if __name__ == "__main__":
    rep = 10
    size = int(sys.argv[1])  # number of digits

    p0time = p1time = p2time = p3time = 0
    for i in range(rep):
        astr = []
        bstr = []
        for j in range(size):
            astr.append(str(random.randint(0, 9)))
            bstr.append(str(random.randint(0, 9)))
        a = int(''.join(astr))
        b = int(''.join(bstr))

        starttime = timeit.default_timer()
        prod0 = multiply_naive(a, b)
        endtime = timeit.default_timer()
        p0time += (endtime - starttime)

        starttime = timeit.default_timer()
        try:
            prod = multiply(a, b)
            endtime = timeit.default_timer()
        except RuntimeError:
            print('cannot run multiply', i)
            prod = -1
            starttime = 0
            endtime = 0
            pass
        p1time += (endtime - starttime)

        starttime = timeit.default_timer()
        n = max(a.bit_length(), b.bit_length())
        prod_dc = multiply_dc(a, b, n)
        endtime = timeit.default_timer()
        p2time += (endtime - starttime)

        starttime = timeit.default_timer()
        prod3 = multiply_nr(a, b)
        endtime = timeit.default_timer()
        p3time += (endtime - starttime)
        print("run", i, a, b, prod0, prod, prod_dc, prod3)

    print(p0time, p1time, p2time, p3time)
