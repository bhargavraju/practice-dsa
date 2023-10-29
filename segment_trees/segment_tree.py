"""
Given an array A of size N and Q queries. Perform following queries:

1 V 0 append V in the back of array.
2 X V set A[X] = V.
3 X 0 delete A[X]. Note: All element at back of X move forward to occupy void.
4 X Y find sum in range [X, Y].
NOTE: For the query of type 4 X Y, output the sum % 10^9 + 7.


Problem Constraints
1 <= N,Q <= 100000
1 <= A[i],V <=100000
1 <= X,Y <= N' Where, N' is current size of array.


Input Format
First argument contains an integer array A.
Second argument contains a Q x 3 Matrix B.


Output Format
Return an integer array containing answer to all query of type 4 X Y in
chronological order.


Example Input
 A = [1, 2, 5, 3, 4]
 B = [ [4, 2, 4],
       [3, 3, 0],
       [1, 6, 0],
       [4, 3, 5] ]


Example Output
 [10, 13]


Example Explanation
 First Query find sum(A[2],A[3],A[4])
 Second Query make A = [1, 2, 3, 4]
 Third Query make A = [1, 2, 3, 4, 6]
 Fourth Query find sum(A[3],A[4],A[5])
"""

import math

# Non-optimal solution, time limit exceeded


# def build(tree, A, idx, s, e):
#     if s == e:
#         tree[idx] = A[s]
#     else:
#         left_child = 2 * idx + 1
#         right_child = 2 * idx + 2
#         mid = (s + e) // 2
#         build(tree, A, left_child, s, mid)
#         build(tree, A, right_child, mid + 1, e)
#         tree[idx] = (tree[left_child] + tree[right_child]) % 1000000007
#
#
# def update(tree, idx, s, e, index, val):
#     if index < s or index > e:
#         return
#     if s == e:
#         tree[idx] = val
#     else:
#         left_child = 2 * idx + 1
#         right_child = 2 * idx + 2
#         mid = (s + e) // 2
#         if s <= index <= mid:
#             update(tree, left_child, s, mid, index, val)
#         if mid + 1 <= index <= e:
#             update(tree, right_child, mid + 1, e, index, val)
#         tree[idx] = (tree[left_child] + tree[right_child]) % 1000000007
#
#
# def query(tree, idx, s, e, l, r):
#     if l <= s and e <= r:
#         return tree[idx]
#     if l > e or s > r:
#         return 0
#     left_child = 2 * idx + 1
#     right_child = 2 * idx + 2
#     mid = (s + e) // 2
#     return (query(tree, left_child, s, mid, l, r) + query(tree, right_child,
#                                                           mid + 1, e, l,
#                                                           r)) % 1000000007
#
#
# def original_index(eff_index, del_arr_tree, total_length, left_index,
#                    left_count):
#     l, r, ans = left_index, total_length - 1, total_length - 1
#     while l <= r:
#         mid = (l + r) // 2
#         deleted_elements = query(del_arr_tree, 0, 0, total_length - 1,
#                                  left_index, mid)
#         if mid - deleted_elements - left_count > eff_index:
#             r = mid - 1
#         elif mid - deleted_elements - left_count < eff_index:
#             l = mid + 1
#         else:
#             ans = mid
#             r = mid - 1
#     return ans
#
#
# class Solution:
#     # @param A : list of integers
#     # @param B : list of list of integers
#     # @return a list of integers
#     def solve(self, A, B):
#         n, m = len(A), len(B)
#         arr = A + [0] * m
#         total_length = n + m
#         h = math.ceil(math.log(total_length, 2))
#         tree_length = (2 ** (h + 1) - 1)
#         arr_tree = [0] * tree_length
#         build(arr_tree, arr, 0, 0, total_length - 1)
#
#         del_arr_tree = [0] * tree_length
#
#         curr_app_index = n
#         res = []
#         for case in B:
#             a, x, y = case[0], case[1], case[2]
#             if a == 1:
#                 update(arr_tree, 0, 0, total_length - 1, curr_app_index, x)
#                 curr_app_index += 1
#             elif a == 2:
#                 eff_index = x - 1
#                 actual_index = original_index(eff_index, del_arr_tree,
#                                               total_length, 0, 0)
#                 update(arr_tree, 0, 0, total_length - 1, actual_index, y)
#             elif a == 3:
#                 eff_index = x - 1
#                 actual_index = original_index(eff_index, del_arr_tree,
#                                               total_length, 0, 0)
#                 update(arr_tree, 0, 0, total_length - 1, actual_index, 0)
#                 update(del_arr_tree, 0, 0, total_length - 1, actual_index, 1)
#             else:
#                 left_eff = x - 1
#                 right_eff = y - 1
#                 left_actual = original_index(left_eff, del_arr_tree,
#                                              total_length, 0, 0)
#                 right_actual = original_index(right_eff, del_arr_tree,
#                                               total_length, left_actual,
#                                               left_actual - left_eff)
#                 ans = (query(arr_tree, 0, 0, total_length - 1, left_actual,
#                              right_actual)) % 1000000007
#                 res.append(ans)
#
#         return res


# Optimal solution

def build(tree, A, idx, s, e):
    if s == e:
        tree[idx] = A[s]
    else:
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        mid = (s + e) // 2
        build(tree, A, left_child, s, mid)
        build(tree, A, right_child, mid + 1, e)
        tree[idx] = (tree[left_child] + tree[right_child]) % 1000000007


def update(tree, idx, s, e, index, val):
    if index < s or index > e:
        return
    if s == e:
        tree[idx] = val
    else:
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        mid = (s + e) // 2
        if s <= index <= mid:
            update(tree, left_child, s, mid, index, val)
        if mid + 1 <= index <= e:
            update(tree, right_child, mid + 1, e, index, val)
        tree[idx] = (tree[left_child] + tree[right_child]) % 1000000007


def query(tree, idx, s, e, l, r):
    if l <= s and e <= r:
        return tree[idx]
    if l > e or s > r:
        return 0
    left_child = 2 * idx + 1
    right_child = 2 * idx + 2
    mid = (s + e) // 2
    return (query(tree, left_child, s, mid, l, r) + query(tree, right_child,
                                                          mid + 1, e, l,
                                                          r)) % 1000000007


def original_index(eff_index, del_arr_tree, total_length, left_index,
                   left_count):
    l, r, ans = left_index, total_length - 1, total_length - 1
    while l <= r:
        mid = (l + r) // 2
        deleted_elements = query(del_arr_tree, 0, 0, total_length - 1,
                                 left_index, mid)
        if mid - deleted_elements - left_count > eff_index:
            r = mid - 1
        elif mid - deleted_elements - left_count < eff_index:
            l = mid + 1
        else:
            ans = mid
            r = mid - 1
    return ans


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n, m = len(A), len(B)
        arr = A + [0] * m
        total_length = n + m
        h = math.ceil(math.log(total_length, 2))
        tree_length = (2 ** (h + 1) - 1)
        arr_tree = [0] * tree_length
        build(arr_tree, arr, 0, 0, total_length - 1)

        del_arr_tree = [0] * tree_length

        curr_app_index = n
        res = []
        for case in B:
            a, x, y = case[0], case[1], case[2]
            if a == 1:
                update(arr_tree, 0, 0, total_length - 1, curr_app_index, x)
                curr_app_index += 1
            elif a == 2:
                eff_index = x - 1
                actual_index = original_index(eff_index, del_arr_tree,
                                              total_length, 0, 0)
                update(arr_tree, 0, 0, total_length - 1, actual_index, y)
            elif a == 3:
                eff_index = x - 1
                actual_index = original_index(eff_index, del_arr_tree,
                                              total_length, 0, 0)
                update(arr_tree, 0, 0, total_length - 1, actual_index, 0)
                update(del_arr_tree, 0, 0, total_length - 1, actual_index, 1)
            else:
                left_eff = x - 1
                right_eff = y - 1
                left_actual = original_index(left_eff, del_arr_tree,
                                             total_length, 0, 0)
                right_actual = original_index(right_eff, del_arr_tree,
                                              total_length, left_actual,
                                              left_actual - left_eff)
                ans = (query(arr_tree, 0, 0, total_length - 1, left_actual,
                             right_actual)) % 1000000007
                res.append(ans)

        return res
