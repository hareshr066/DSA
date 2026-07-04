#Minimum no of days to make m bouquets :
def minDays(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1

    def canmake(day):
        bouquets = 0
        flowers = 0

        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1

                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0

        return bouquets >= m

    low, high = min(bloomDay), max(bloomDay)
    res = -1

    while low <= high:
        mid = (low + high) // 2

        if canmake(mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res


# Input
bloomDay = list(map(int, input("Enter bloom days: ").split()))
m = int(input("Enter number of bouquets (m): "))
k = int(input("Enter flowers per bouquet (k): "))

# Output
result = minDays(bloomDay, m, k)
print("Minimum days required:", result)