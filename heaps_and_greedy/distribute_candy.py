"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following
requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?


Problem Constraints
1 <= N <= 10^5
-109 <= A[i] <= 10^9


Input Format
First and only argument is an integer array A representing the
rating of children.


Output Format
Return an integer, representing the minimum candies to be given.


Example Input
Input 1:
 A = [1, 2]
Input 2:
 A = [1, 5, 2, 1]


Example Output
Output 1:
 3
Output 2:
 7


Example Explanation
Explanation 1:
 The candidate with 1 rating gets 1 candy and candidate with rating 2 cannot
 get 1 candy as 1 is its neighbor. So rating 2 candidate gets 2 candies.
 In total, 2 + 1 = 3 candies need to be given out.
Explanation 2:
 Candies given = [1, 3, 2, 1]
"""


# @param A : list of integers
# @return an integer
def candy(A):
    n = len(A)

    candies = [1] * n
    for i in range(1, n):
        if A[i] > A[i - 1]:
            candies[i] = max(candies[i], candies[i - 1] + 1)

    for i in range(n - 2, -1, -1):
        if A[i] > A[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)
