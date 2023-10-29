"""
There are two sorted arrays A and B of size N and M respectively.
Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

NOTE:
The overall run time complexity should be O(log (m+n)).
IF the number of elements in the merged array is even, then the median is the average of (n/2)th and (n/2+1)th element.
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5.

Solution explanation:
i1 -> number of elements picked from the smaller array to the left half (of the combined array),
    can have values [0, len(arr)],
    is the index of the first (and min) number of the numbers picked from the smaller array to the right half

i2 -> number of elements picked from the larger array to the left half (of the combined array)

max1 -> max of the left partition of the smaller array
min1 -> min of the right partition of the smaller array
max2 -> max of the left partition of the bigger array
min2 -> min of the right partition of the bigger array

We can determine we found the right partition if the max of left partitions of both arrays is less than or equal to
min of right partitions of both the arrays
"""


# @param A : tuple of integers
# @param B : tuple of integers
# @return a double
def findMedianSortedArrays(A, B):
    (short_arr, long_arr) = (B, A) if len(B) < len(A) else (A, B)
    len_short, len_long = len(short_arr), len(long_arr)
    left, right = 0, len_short
    while left <= right:
        i1 = (left + right)//2
        i2 = (len_short + len_long + 1)//2 - i1

        max1 = float('-inf') if i1 == 0 else short_arr[i1 - 1]
        min1 = float('inf') if i1 == len_short else short_arr[i1]
        max2 = float('-inf') if i2 == 0 else long_arr[i2 - 1]
        min2 = float('inf') if i2 == len_long else long_arr[i2]

        if max2 > min1:
            left = i1 + 1
        elif max1 > min2:
            right = i1 - 1
        else:
            if (len_short + len_long) % 2 == 0:
                return (max(max1, max2) + min(min1, min2)) / 2
            else:
                return float(max(max1, max2))
