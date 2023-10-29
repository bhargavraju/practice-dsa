"""
Given a binary string A of size N and an integer matrix B of size Q x 3.

Matrix B has Q queries:

For queries of type B[i][0] = 1, flip the value at index B[i][1] in A
if and only if the value at that index is 0 and return -1.
For queries of type B[i][0] = 0, Return the value of the binary string from
index B[i][1] to B[i][2] modulo 3.
Note: Rows are numbered from top to bottom and
columns are numbered from left to right.


Input Format
The first argument given is the string A.
The second argument given is the integer matrix B of size Q * 3.

Output Format
Return an array of size Q where ith value is answer to ith query.


Example Input

Input 1:
 A = 10010
 B = [  [0, 3, 5]
        [0, 3, 4]
        [1, 2, -1]
        [0, 1, 5]
     ]

Input 2:
 A = 11111
 B = [
        [0, 2, 4]
        [1, 2, -1
        [0, 2, 4]]
     ]


Example Output

Output 1:
 [2, 1, -1, 2]
Output 2:
 [1, -1, 1]


Example Explanation

Explanation 1:
 For query 1, binary string from index 3 to 5 is 010 = 2. So 2 mod 3 = 2.
 For query 2, binary string from index 3 to 4 is 01 = 1. So 1 mod 3 = 1.
 After query 3, given string changes to 11010.
 For query 4, binary string from index 1 to 5 is 11010 = 26. So 26 mod 3 = 2.
 So, output array is [2, 1, -1, 2].

Explanation 2:
 For query 1, binary string from index 2 to 4 is 111 = 7. So 7 od 3 = 1.
 After query 2, string remains same as there is already 1 at index 2.
 For query 3, binary string from index 2 to 4 is 111 = 7. So 7 od 3 = 1.
 So, output array is [1, -1, 1].
"""

import math


def build(tree, A, idx, s, e):
    if s == e:
        tree[idx] = int(A[s])
    else:
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        mid = (s + e) // 2
        build(tree, A, left_child, s, mid)
        build(tree, A, right_child, mid + 1, e)
        power_modulo = 1 if (e - mid) & 1 == 0 else 2
        tree[idx] = ((tree[left_child] * power_modulo) % 3 + tree[
            right_child]) % 3


def update(tree, idx, s, e, index):
    if index < s or index > e:
        return
    if s == e:
        tree[idx] = 1
    else:
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        mid = (s + e) // 2
        update(tree, left_child, s, mid, index)
        update(tree, right_child, mid + 1, e, index)
        power_modulo = 1 if (e - mid) & 1 == 0 else 2
        tree[idx] = ((tree[left_child] * power_modulo) % 3 + tree[
            right_child]) % 3


def query(tree, idx, s, e, l, r):
    if l <= s and e <= r:
        return tree[idx]
    if e < l or r < s:
        return 0
    left_child = 2 * idx + 1
    right_child = 2 * idx + 2
    mid = (s + e) // 2
    left = query(tree, left_child, s, mid, l, r)
    right = query(tree, right_child, mid + 1, e, l, r)
    power_modulo = 1 if (min(e, r) - mid) & 1 == 0 else 2
    return ((left * power_modulo) % 3 + right) % 3 if min(e,
                                                          r) >= mid else left


class Solution:
    # @param A : string
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        h = math.ceil(math.log(n, 2))
        tree_length = (2 ** (h + 1)) - 1
        segment_tree = [0] * tree_length
        build(segment_tree, A, 0, 0, n - 1)
        ans = []
        for case in B:
            if case[0] == 0:
                ans.append(
                    query(segment_tree, 0, 0, n - 1, case[1] - 1, case[2] - 1))
            else:
                update(segment_tree, 0, 0, n - 1, case[1] - 1)
                ans.append(-1)
        return ans
