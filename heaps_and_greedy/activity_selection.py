"""
Given two integer arrays A and B of size N. There are N activities where
A[i] denotes the start time of the ith activity and B[i] denotes the finish
time of the ith activity. Your task is to select the maximum number of
activities that can be performed by a single person, assuming that a person
can only work on a single activity at a time.
"""


# @param A : list of integers
# @param B : list of integers
# @return an integer
def solve(A, B):
    n = len(A)
    tasks = [(A[i], B[i]) for i in range(n)]
    tasks.sort(key=lambda x: x[1])
    res = []
    for task in tasks:
        if res:
            last = res[-1]
            if task[0] >= last[1]:
                res.append(task)
        else:
            res.append(task)
    return len(res)
