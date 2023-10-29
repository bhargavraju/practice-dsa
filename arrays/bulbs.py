"""
N light bulbs are connected by a wire.
Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the
bulbs to the right of current bulb.

Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
You can press the same switch multiple times.

Note: 0 represents the bulb is off and 1 represents the bulb is on.

Problem Constraints
1 <= N <= 5*105
0 <= A[i] <= 1
"""


def bulbs(A):
    flips, count, n = 0, 0, len(A)
    for i in range(n):
        if (A[i] == 1 and flips % 2 == 0) or (A[i] == 0 and flips % 2 == 1):
            continue
        elif (A[i] == 0 and flips % 2 == 0) or (A[i] == 1 and flips % 2 == 1):
            flips += 1
            count += 1
    return count
