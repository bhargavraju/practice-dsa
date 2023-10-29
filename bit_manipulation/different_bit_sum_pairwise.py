"""
We define f(X, Y) as number of different corresponding bits in binary representation of X and Y.
For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively.
The first and the third bit differ, so f(2, 7) = 2.

You are given an array of N positive integers, A1, A2 ,..., AN.
Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 231 - 1
"""


# Solution 1
def setBitCount(num):
    count = 0
    while num > 0:
        num = num & (num-1)
        count += 1
    return count


# @param A : list of integers
# @return an integer
def cntBits(A):
    total = 0
    n = len(A)
    for i in range(n):
        for j in range(n):
            xor = A[i] ^ A[j]
            total = (total + setBitCount(xor)) % 1000000007
    return total


# Solution 2
# @param A : list of integers
# @return an integer
def cntBits2(A):
    total = 0
    bit_checker = 1
    for i in range(32):
        ones_count = 0
        for num in A:
            if num & bit_checker != 0:
                ones_count += 1
        total = (total + ones_count * (len(A) - ones_count) * 2) % 1000000007
        bit_checker = bit_checker << 1
    return total % 1000000007


test = [1, 3, 5]
ans = cntBits(test)
print(ans)
