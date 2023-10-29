"""
Given an array A of N integers, find the index of values that satisfy P + Q = R + S,
where P,Q,R & S are integers values in the array, Expected time complexity O(N2)

NOTE:
1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1

2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices in the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 if:
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
If no solution is possible, return an empty list.
"""


# @param A : list of integers
# @return a list of integers
def equal(A):
    sum_pair_map = {}
    n = len(A)
    ans = []

    def is_better_solution(l):
        return l < ans

    for i in range(n):
        for j in range(i + 1, n):
            pair_sum = A[i] + A[j]
            if pair_sum in sum_pair_map:
                a, b = sum_pair_map[pair_sum]
                if a < i and b != i and b != j and (not ans or is_better_solution([a, b, i, j])):
                    ans = [a, b, i, j]
            else:
                sum_pair_map[pair_sum] = (i, j)
    return ans
