"""
Given a positive integer A, the task is to count the total number of set bits in the binary representation of
all the numbers from 1 to A. Return the count modulo 10^9 + 7.

Problem Constraints
1 <= A <= 109

Good explanation of solution at:
https://www.youtube.com/watch?v=g6OxU-hRGtY&ab_channel=Pepcoding
"""


def largest_power_of_2_in_range(num):
    x = 0
    while (1 << x) <= num:
        x += 1
    return x - 1


# @param A : integer
# @return an integer
def solve(A):
    if A == 0:
        return 0
    x = largest_power_of_2_in_range(A)
    bits_till_2_power_x = x * (1 << x) // 2
    left_most_bits_from_2_power_x = A - (1 << x) + 1
    remaining_no_to_solve_for = A - (1 << x)
    return (bits_till_2_power_x + left_most_bits_from_2_power_x + solve(remaining_no_to_solve_for)) % 1000000007
