"""
Given a matrix B, of size N x M, you are allowed to do at most A special
operations on this grid such that there is no vertical or horizontal
contiguous subarray that has a sum greater than C.

A special operation involves multiplying any element by -1 i.e.
changing its sign.

Return 1 if it is possible to achieve the answer, otherwise 0.

Problem Constraints
1 <= N, M <= 10
0 <= A <= 5
-10^5 <= B[i][j], C <= 10^5

Input Format
The first argument is an integer A, representing the number of
special operations allowed.
The second argument has the N x M integer matrix, B.
The third argument is an integer C, as described in the problem statement.

Output Format
Return 1 if it is possible to achieve the answer, otherwise 0.

Example Input

Input 1:
 A = 3
 B = [
        [1, 1, 1]
        [1, 1, 1]
        [1, 1, 1]
     ]
 C = 2

Input 2:
 A = 1
 B = [
        [1, 1, 1]
        [1, 1, 1]
        [1, 1, 1]
     ]
 C = 2

Example Output

Output 1:
 1

Output 2:
 0
"""


class Solution:

    def rec_helper(self, ops, B, C):
        if ops == -1:
            return False
        res = True

        for i in range(len(B)):
            for j in range(len(B[0])):
                total = 0
                for k in range(j, len(B[0])):
                    total += B[i][k]
                    if total > C:
                        res = False
                        for l in range(j, k+1):
                            if B[i][l] > 0:
                                B[i][l] = -B[i][l]
                                res = res or self.rec_helper(ops-1, B, C)
                                B[i][l] = -B[i][l]
                        return res

        for j in range(len(B[0])):
            for i in range(len(B)):
                total = 0
                for k in range(i, len(B)):
                    total += B[k][j]
                    if total > C:
                        res = False
                        for l in range(i, k+1):
                            if B[l][j] > 0:
                                B[l][j] = -B[l][j]
                                res = res or self.rec_helper(ops-1, B, C)
                                B[l][j] = -B[l][j]
                        return res

        return res

    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return int(self.rec_helper(A, B, C))
