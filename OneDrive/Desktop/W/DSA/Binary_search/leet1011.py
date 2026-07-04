# capacity to ship packages within D days !!
def shipWithinDays(weights, days):
    low, high = max(weights), sum(weights)
    res = float('inf')

    while low <= high:
        mid = (low + high) // 2
        tot = 0
        d = 1

        for i in weights:
            if tot + i <= mid:
                tot += i
            else:
                d += 1
                tot = i

        if d <= days:
            res = min(res, mid)
            high = mid - 1
        else:
            low = mid + 1

    return res

weights = list(map(int, input("Enter the weights: ").split()))
days = int(input("Enter the number of days: "))

print("Minimum ship capacity:", shipWithinDays(weights, days))