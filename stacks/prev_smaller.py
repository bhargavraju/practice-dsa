"""
Given an array A, find the nearest smaller element G[i] for every element A[i] in the array such that
the element has an index smaller than i.

More formally,
G[i] for an element A[i] = an element A[j] such that
j is maximum possible AND
j < i AND
A[j] < A[i]

Elements for which no smaller element exist, consider next smaller element as -1.
"""


# @param A : list of integers
# @return a list of integers
def prevSmaller(A):
    n = len(A)
    st = []
    left_smaller = [-1] * n
    for i in range(n):
        while len(st) > 0 and st[-1] >= A[i]:
            st.pop()
        if len(st) > 0:
            left_smaller[i] = st[-1]
        st.append(A[i])
    return left_smaller
