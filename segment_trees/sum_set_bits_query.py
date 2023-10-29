"""
Bob has an array A of N integers. Initially, all the elements
of the array are zero. Bob asks you to perform Q operations on this array.

You have to perform three types of query,
in each query you are given three integers x, y and z.

if x = 1: Update the value of A[y] to 2 * A[y] + 1.
if x = 2: Update the value A[y] to ⌊A[y]/2⌋ ,
    where ⌊⌋ is Greatest Integer Function.
if x = 3: Take all the A[i] such that y <= i <= z and
convert them into their corresponding binary strings.
Now concatenate all the binary strings and
find the total no. of '1' in the resulting string.

Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x,
B[i][1] denotes y, B[i][2] denotes z.

Problem Constraints
1 <= N, Q <= 100000
1 <= y, z <= N
1 <= x <= 3


Input Format
The first argument has the integer A.
The second argument is a 2d matrix B, of size Q x 3, representing the queries.

Output Format
Return an array of integers where ith index represents
the answer of the ith type 3 query.


Example Input

Input 1:
 A = 5
 B = [
        [1, 1, -1]
        [1, 2, -1]
        [1, 3, -1]
        [3, 1, 3]
        [3, 2, 4]
     ]
Input 2:
 A = 5
 B = [
        [1, 1, -1]
        [1, 2, -1]
        [3, 1, 3]
        [2, 1, -1]
        [3, 1, 3]
     ]


Example Output

Output 1:
 [3, 2]
Output 2:
 [2, 1]


Example Explanation

Explanation 1:
 Initial array A = [0, 0, 0, 0, 0]
 After query 1, A => [1, 0, 0, 0, 0]
 After query 2, A => [1, 1, 0, 0, 0]
 After query 3, A => [1, 1, 1, 0, 0]
 For query 4, Concatenation of Binary String between index 1 and 3 : 111.
    So, number of 1's = 3
 For query 5, Concatenation of Binary String between index 2 and 4 : 110.
    So, number of 1's = 2
 So, output array is [3, 2].

Explanation 2:
 Initial array A = [0, 0, 0, 0, 0]
 After query 1, A => [1, 0, 0, 0, 0]
 After query 2, A => [1, 1, 0, 0, 0]
 For query 3, Concatenation of Binary String between index 1 and 3 : 110.
    So, number of 1's = 2
 After query 4, A => [0, 1, 0, 0, 0]
 For query 5, Concatenation of Binary String between index 2 and 4 : 010.
    So, number of 1's = 1.
 So, output array is [2, 1].
"""


import math


def no_of_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


def build(tree, A, idx, s, e):
    if s == e:
        tree[idx] = no_of_set_bits(A[s])
    else:
        left_child = 2*idx + 1
        right_child = 2*idx + 2
        mid = (s+e)//2
        build(tree, A, left_child, s, mid)
        build(tree, A, right_child, mid+1, e)
        tree[idx] = tree[left_child] + tree[right_child]


def update(tree, idx, s, e, index, val):
    if index < s or index > e:
        return
    if s == e:
        tree[idx] = no_of_set_bits(val)
    else:
        left_child = 2*idx + 1
        right_child = 2*idx + 2
        mid = (s+e)//2
        update(tree, left_child, s, mid, index, val)
        update(tree, right_child, mid+1, e, index, val)
        tree[idx] = tree[left_child] + tree[right_child]


def query(tree, idx, s, e, l, r):
    if l <= s and r >= e:
        return tree[idx]
    if l > e or r < s:
        return 0
    left_child = 2*idx + 1
    right_child = 2*idx + 2
    mid = (s+e)//2
    return query(tree, left_child, s, mid, l, r) + query(tree, right_child, mid+1, e, l, r)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        arr = [0]*A
        height = math.ceil(math.log(A, 2))
        segment_tree_length = (2**(height+1))-1
        segment_tree = [0]*segment_tree_length
        build(segment_tree, arr, 0, 0, A-1)
        res = []
        for case in B:
            x, y, z = case[0], case[1], case[2]
            if x == 1:
                update(segment_tree, 0, 0, A-1, y-1, 2*arr[y-1]+1)
                arr[y-1] = 2*arr[y-1]+1
            elif x == 2:
                update(segment_tree, 0, 0, A-1, y-1, arr[y-1]//2)
                arr[y-1] = arr[y-1]//2
            else:
                ans = query(segment_tree, 0, 0, A-1, y-1, z-1)
                res.append(ans)
        return res
