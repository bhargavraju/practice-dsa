"""
Given a binary tree A.
Check whether it is possible to partition the tree to two trees_and_tries which have
equal sum of values after removing exactly one edge on the original tree.


Problem Constraints
1 <= size of tree <= 100000
-10^9 <= value of node <= 10^9

Input Format
First and only argument is head of tree A.

Output Format
Return 1 if the tree can be partitioned into
two trees_and_tries of equal sum else return 0.


Example Input
Input 1:


                5
               /  \
              3    7
             / \  / \
            4  6  5  6
Input 2:


                1
               / \
              2   10
                  / \
                 20  2


Example Output

Output 1:
 1
Output 2:
 0


Example Explanation

Explanation 1:
 Remove edge between 5(root node) and 7:
        Tree 1 =                                               Tree 2 =
                        5                                                     7
                       /                                                     / \
                      3                                                     5   6
                     / \
                    4   6
        Sum of Tree 1 = Sum of Tree 2 = 18

Explanation 2:
 The given Tree cannot be partitioned.
"""


def rec_sum(node):
    left_sum = rec_sum(node.left) if node.left else 0
    right_sum = rec_sum(node.right) if node.right else 0

    node.val = node.val + left_sum + right_sum
    return node.val


def is_present(node, val, A):
    if node is not A and node.val == val / 2:
        return True

    if node.left and is_present(node.left, val, A):
        return True
    if node.right and is_present(node.right, val, A):
        return True

    return False


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        total_sum = rec_sum(A)
        ans = is_present(A, total_sum, A)
        return int(ans)
