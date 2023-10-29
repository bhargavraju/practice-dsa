BIT = [[0 for i in range(200005)] for j in range(2)]
ar = [0] * 200005
n = 0
t = 0
maxN = 200005
mod = 1e9 + 7


def update(i, x, delta):
    global BIT, maxN
    while x < maxN:
        BIT[i][x] += delta
        x += x & (-x)


def query(i, x):
    global BIT, maxN
    summ = 0
    while x > 0:
        summ += BIT[i][x]
        x -= x & (-x)
    return summ


def getidx(x):
    lo = 1
    hi = n
    idx = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        qu = query(1, mid)
        if (x + qu) == mid:
            idx = mid
            hi = mid - 1
        elif (x + qu) < mid:
            hi = mid - 1
        else:
            lo = mid + 1
    return idx


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        global BIT, ar, maxN, n, t
        n = len(A)
        BIT = [[0 for i in range(200005)] for j in range(2)]
        ar = [0] * 200005
        for i in range(1, n + 1):
            ar[i] = A[i - 1]
            update(0, i, ar[i])
        ans = []
        for i in B:
            t = i[0]
            if t == 1:
                n += 1
                ar[n] = i[1]
                update(0, n, ar[n])
            if t == 2:  # update ar[x] to Y
                x = i[1]
                y = i[2]
                idx = getidx(x)
                update(0, idx, y - ar[idx])
                ar[idx] = y

            if t == 3:  # delete ar[x]
                x = i[1]
                idx = getidx(x)
                update(0, idx, -ar[idx])
                update(1, idx, 1)
            if t == 4:  # query sum in [X,Y]
                idx1 = 0
                idx2 = 0
                x = i[1]
                y = i[2]
                idx1 = getidx(x)
                idx2 = getidx(y)
                val = query(0, idx2) - query(0, idx1 - 1)
                val = val % mod
                val = int(val)
                ans.append(val)
        return ans
