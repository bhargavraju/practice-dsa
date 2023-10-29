"""
Given an array, A find the next greater element G[i] for every element A[i] in the array.
The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array, A.

More formally:
G[i] for an element A[i] = an element A[j] such that
    j is minimum possible AND
    j > i AND
    A[j] > A[i]

Elements for which no greater element exist, consider next greater element as -1.

Problem Constraints
1 <= |A| <= 10^5
1 <= A[i] <= 10^7
"""


# @param A : list of integers
# @return a list of integers
def nextGreater(A):
    n = len(A)
    st = []
    next_greater = [-1] * n

    for i in range(n - 1, -1, -1):
        while len(st) > 0 and st[-1] <= A[i]:
            st.pop()
        if len(st) > 0:
            next_greater[i] = st[-1]
        st.append(A[i])

    return next_greater
