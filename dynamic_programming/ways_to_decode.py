"""
A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the
total number of ways to decode it modulo 109 + 7.

Problem Constraints
1 <= length(A) <= 10^5
"""


# @param A : string
# @return an integer
def numDecodings(A):
    n = len(A)
    ways = [0]*(n+1)
    ways[0] = 1
    ways[1] = 0 if int(A[0]) == 0 else 1
    for i in range(2, n+1):
        single_num = int(A[i-1])
        double_num = int(A[i-2] + A[i-1])
        if 10 <= double_num <= 26:
            ways[i] = (ways[i] + ways[i-2]) % 1000000007
        if single_num >= 1:
            ways[i] = (ways[i] + ways[i-1]) % 1000000007
    return ways[n]
