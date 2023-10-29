"""
Given an array A, containing positive integers. You need to perform some
queries on it. You will be given Q Queries. Each query will have
one string and two integers.

Each Query can be of two type :
"C" X Y - Here "C" says that we need to Change the integer at position X to integer Y.
"A" X Y - Here "A" say that we are Asked number of primes in the the range : [X, Y] (inclusive)
For each Query of type 2, you need to calculate an integer denoting the answer to it.

NOTE:
Assume 1-indexing for all queries.
Your code will be run on multiple test cases (< 10). Make sure to come up
with an optimised solution and take care of clearing global variables.

Problem Constraints
1 <= Size of A <= 4 * 10^4
1 <= A[i] <= 10^6
1 <= Number of Queries (Size of B, C, D) <= 5 * 10^4

Input Format
First argument is an integer array A.
Second argument is a string array B.
Third argument is an integer array C.
Fourth argument is an integer array D.
In the i-th query, B[i] denotes the string, C[i] denotes X and D[i] denotes Y.

Output Format
Return an integer array, where each of the element represents
the answer to the queries of type 2, in chronological order.


Example Input
Input 1:
 A = [1, 3, 121, 20, 17, 26, 29]
 B = ["A", "C", "A"]
 C = [1, 3,  1]
 D = [7, 19, 7]
Input 2:
 A = [7, 15, 11]
 B = ["C", "A"]
 C = [2, 2]
 D = [9, 3]


Example Output
Output 1:
 [3, 4]
Input 2:
 [1]


Example Explanation
Explanation 1:
 Given array A = [1, 3, 121, 20, 17, 26, 29]. Let's list down queries:
 1. A 1 7 :  Number of primes in complete array [1-7] is 3 => 3, 17, 29
 2. C 3 19 : Change the number at index-3 to 19. So Array becomes :
                [1, 3, 19, 20, 17, 26, 29]
 3. A 1 7 : Number of primes in complete array [1-7] is 4 => 3, 19, 17, 29
 So output : [3, 4]
Explanation 2:
 Given array A = [7, 15, 11]. Let's list down queries:
 1. C 2 9 :  Change the number at index-2 to 9. So Array becomes : [7, 9, 11]
 2. A 2 3 : Number of primes in array [2 - 3] is 1 => 11
 So output : [1]

"""


import math


def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 0
        return 1
    else:
        return 0


def build(tree, A, idx, s, e):
    if s == e:
        tree[idx] = is_prime(A[s])
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
        tree[idx] = val
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
    if e < l or r < s:
        return 0
    left_child = 2*idx + 1
    right_child = 2*idx + 2
    mid = (s+e)//2
    return query(tree, left_child, s, mid, l, r) + query(tree, right_child, mid+1, e, l, r)


class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @param C : list of integers
    # @param D : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D):
        n = len(A)
        h = math.ceil(math.log(n, 2))
        seg_length = (2**(h+1)-1)
        seg_tree = [0]*seg_length
        build(seg_tree, A, 0, 0, n-1)
        res = []
        for i in range(len(B)):
            x, y, z = B[i], C[i], D[i]
            if x == 'C':
                index = y-1
                prev_prime = is_prime(A[index])
                curr_prime = is_prime(z)
                if prev_prime ^ curr_prime:
                    update(seg_tree, 0, 0, n-1, index, curr_prime)
                A[index] = z
            else:
                ans = query(seg_tree, 0, 0, n-1, y-1, z-1)
                res.append(ans)
        return res
