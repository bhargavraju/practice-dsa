"""
Given an integer array A of size N.

You have to perform two types of query, in each query
you are given three integers x,y,z.

If x = 0, then update A[y] = z.
If x = 1, then output the minimum element in the array A
between index y and z inclusive. (Indexes are 1 based in the input)
Queries are denoted by a 2-D array B of size M x 3 where
B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.


Problem Constraints
1 <= N, M <= 10^5
1 <= A[i] <= 10^9

If x = 0, 1<= y <= N and 1 <= z <= 10^9
If x = 1, 1<= y <= z <= N


Input Format
First argument is an integer array A of size N.
Second argument is a 2-D array B of size M x 3 denoting queries.


Output Format
Return an integer array denoting the output of each query where value of x is 1


Example Input

Input 1:
 A = [1, 4, 1]
 B = [
        [1, 1, 3]
        [0, 1, 5]
        [1, 1, 2]
     ]

Input 2:
 A = [5, 4, 5, 7]
 B = [
        [1, 2, 4]
        [0, 1, 2]
        [1, 1, 4]
     ]


Example Output

Output 1:
 [1, 4]

Output 2:
 [4, 2]


Example Explanation

Explanation 1:
 For 1st query, the minimum element from range (1, 3) is 1.
 For 2nd query, update A[1] = 5, now A = [5, 4, 1].
 For 3rd query, the minimum element from range (1, 2) is 4.

Explanation 2:
 For 1st query, the minimum element from range (2, 4) is 4.
 For 2nd query, update A[1] = 2, now A = [2, 4, 5, 7].
 For 3rd query, the minimum element from range (1, 4) is 2.
"""


import math


def build(tree, A, idx, s, e):
    if s == e:
        tree[idx] = A[s]
    else:
        left_child = 2*idx+1
        right_child = 2*idx+2
        mid = (s+e)//2
        build(tree, A, left_child, s, mid)
        build(tree, A, right_child, mid+1, e)
        tree[idx] = min(tree[left_child], tree[right_child])


def query(tree, idx, s, e, l, r):
    if l <= s and e <= r:
        return tree[idx]
    if l > e or r < s:
        return float('inf')
    left_child = 2*idx+1
    right_child = 2*idx+2
    mid = (s+e)//2
    return min(query(tree, left_child, s, mid, l, r), query(tree, right_child, mid+1, e, l, r))


def update(tree, idx, s, e, index, val):
    if index < s or index > e:
        return
    if s == e:
        tree[idx] = val
    else:
        left_child = 2*idx+1
        right_child = 2*idx+2
        mid = (s+e)//2
        update(tree, left_child, s, mid, index, val)
        update(tree, right_child, mid+1, e, index, val)
        tree[idx] = min(tree[left_child], tree[right_child])


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        h = math.ceil(math.log(n, 2))
        segment_length = (2**(h+1))-1
        segment_tree = [0]*segment_length
        build(segment_tree, A, 0, 0, n-1)
        ans = []
        for case in B:
            if case[0] == 0:
                index = case[1]-1
                val = case[2]
                update(segment_tree, 0, 0, n-1, index, val)
            else:
                l, r = case[1]-1, case[2]-1
                res = query(segment_tree, 0, 0, n-1, l, r)
                ans.append(res)
        return ans
