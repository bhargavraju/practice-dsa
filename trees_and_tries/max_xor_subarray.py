"""
Problem Description

Given an array A of integers of size N. Find the subarray
AL, AL+1, AL+2, ... AR with 1<=L<=R<=N which has maximum XOR value.

NOTE: If there are multiple subarrays with same maximum value,
return the subarray with minimum length.
If length is same, return the subarray with minimum starting index.

Problem Constraints
1 <= N <= 100000
0 <= A[i] <= 10^9

Input Format
First and only argument is an integer array A.

Output Format
Return an integer array B of size 2.
 B[0] is the starting index(1-based) of the subarray and
 B[1] is the ending index(1-based) of the subarray.


Example Input
Input 1:
 A = [1, 4, 3]

Input 2:
 A = [8]

Example Output
Output 1:
 [2, 3]

Output 2:
 [1, 1]


Example Explanation

Explanation 1:
 There are 6 possible subarrays of A:
 subarray            XOR value
 [1]                     1
 [4]                     4
 [3]                     3
 [1, 4]                  5 (1^4)
 [4, 3]                  7 (4^3)
 [1, 4, 3]               6 (1^4^3)

 [4, 3] subarray has maximum XOR value. So, return [2, 3].

Explanation 2:
 There is only one element in the array. So, the maximum XOR value
 is equal to 8 and the only possible subarray is [1, 1].
"""


class Trie:

    def __init__(self):
        self.left = None
        self.right = None
        self.indices = []


def insert(trie, num):
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
    return curr


def compare(trie, num):
    curr = trie
    xor_value = 0
    for i in range(31, -1, -1):
        bit = (1 << i) & num
        if bit == 0:
            if curr.right is not None:
                xor_value += (1 << i)
                curr = curr.right
            else:
                curr = curr.left
        else:
            if curr.left is not None:
                xor_value += (1 << i)
                curr = curr.left
            else:
                curr = curr.right
    return xor_value, curr


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        total_xor = 0
        trie = Trie()
        node = insert(trie, 0)
        node.indices.append(0)
        max_xor = float('-inf')
        ans = [len(A) - 1, len(A) - 1]
        for i in range(len(A)):
            total_xor ^= A[i]
            insert_leaf = insert(trie, total_xor)
            insert_leaf.indices.append(i + 1)
            xor_value, compare_leaf = compare(trie, total_xor)
            best_index = max(compare_leaf.indices)
            if xor_value > max_xor:
                max_xor = xor_value
                ans = best_index, i
            elif xor_value == max_xor:
                curr_length = i - best_index
                existing_length = ans[1] - ans[0]
                if curr_length < existing_length or \
                        (curr_length == existing_length and
                         best_index < ans[0]):
                    ans = best_index, i

        return list(map(lambda x: x + 1, ans))
