"""
Given an array of integers A and an integer B.
We need to reverse the order of the first B elements of the array,
leaving the other elements in the same relative order.

NOTE: You are required to first insert elements into an auxiliary queue
then perform Reversal of first B elements.
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        st = []
        for i in range(B):
            st.append(A[i])

        for i in range(B):
            A[i] = st.pop()

        return A
