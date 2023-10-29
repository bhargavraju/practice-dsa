"""
Given two integer arrays A and B of size N. There are N jobs every job has a
deadline and associated profit if the job is finished before the deadline.
A[i] denotes the deadline of the ith job and B[i] denotes the
associated profit with ith job.

Every job takes single unit of time, so
the minimum possible deadline for any job is 1.

Your task is to schedule jobs such that maximum profit is achieved if
only one job can be scheduled at a time.
"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        tasks = sorted([(B[i], A[i]) for i in range(n)], reverse=True)
        max_days = max(A)
        days = [False for _ in range(max_days)]
        total_profit = 0
        for task in tasks:
            profit = task[0]
            day = task[1]
            for i in range(day-1, -1, -1):
                if days[i] is False:
                    days[i] = True
                    total_profit += profit
                    break
        return total_profit
