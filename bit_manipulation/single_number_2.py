"""
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.

NOTE: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Refer these resources for solution explanation
https://www.youtube.com/watch?v=3gJxLkPPW6M&ab_channel=Pepcoding
https://www.geeksforgeeks.org/find-the-element-that-appears-once/
"""


def singleNumber(A):
    ones, twos = 0, 0
    for num in A:
        twos = twos | (ones & num)
        ones = ones ^ num
        common_bit_mask = ~(ones & twos)
        ones &= common_bit_mask
        twos &= common_bit_mask
    return ones
