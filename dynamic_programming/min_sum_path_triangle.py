"""
Given a triangle, find the minimum path sum from top to bottom. Each step you
may move to adjacent numbers on the row below.

Adjacent numbers for jth number of row i is jth and (j+1)th numbers of row i+1


Problem Constraints
|A| <= 1000
A[i] <= 1000

Input Format
First and only argument is the vector of vector A defining the given triangle

Output Format
Return the minimum sum

Example Input
Input 1:
A = [
         [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]
Input 2:
 A = [ [1] ]

Example Output
Output 1:
 11
Output 2:
 1
"""


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                A[i][j] = min(A[i+1][j] + A[i][j], A[i+1][j+1] + A[i][j])
        return A[0][0]
