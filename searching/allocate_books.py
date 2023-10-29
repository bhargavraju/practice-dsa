"""
Given an array of integers A of size N and an integer B.
College library has N books,the ith book has A[i] number of pages.
You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.

Problem Constraints
1 <= N <= 105
1 <= A[i], B <= 105
"""


# @param A : list of integers
# @param B : integer
# @return an integer
def books(A, B):
    def is_possible(k):
        students = 1
        count = 0
        for i in range(len(A)):
            if A[i] > k:
                return False
            if count + A[i] > k:
                count = A[i]
                students += 1
                if students > B:
                    return False
            else:
                count += A[i]
        return True

    if len(A) < B:
        return -1

    left, right, ans = max(A), sum(A), sum(A)
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
