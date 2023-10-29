"""
Given an array of integers A, find and return the maximum result of
A[i] XOR A[j], where i, j are the indexes of the array.

Problem Constraints
1 <= length of the array <= 100000
0 <= A[i] <= 10^9
"""


class Trie:

    def __init__(self):
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Build a trie(tree) which stores all numbers in binary
        trie = Trie()
        for num in A:
            curr = trie
            for i in range(31, -1, -1):
                bit = (1 << i) & num

                if bit == 0:
                    if curr.left is None:
                        curr.left = Trie()
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Trie()
                    curr = curr.right
        # For each number check the max possible xor using the pre-built trie
        max_xor = 0
        for num in A:
            curr = trie
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (1 << i) & num

                if bit == 0:
                    if curr.right is not None:
                        curr_xor += (1 << i)
                        curr = curr.right
                    else:
                        curr = curr.left
                else:
                    if curr.left is not None:
                        curr_xor += (1 << i)
                        curr = curr.left
                    else:
                        curr = curr.right

            max_xor = max(max_xor, curr_xor)

        return max_xor

