def valid_attendance(n):
    if n < 1:
        print("Invalid input")
        return
    if 1 <= n < 3:
        print(2*n, "{}/{}".format(n, 2*n))
        return
    c1, c2, c3, c4 = 1, 1, 1, 1
    for i in range(3, n+1):
        c1, c2, c3, c4 = c3, c1+c3, c2+c4, c2+c4
    total_ways = c1+c2+c3+c4
    ways_to_miss_graduation = c1+c3
    print(total_ways, "{}/{}".format(ways_to_miss_graduation, total_ways))


no_of_days = int(input("Enter no of days: "))
valid_attendance(no_of_days)
