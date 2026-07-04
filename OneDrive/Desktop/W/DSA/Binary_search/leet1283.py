# finding the smallest divisor !!
from math import ceil

def smallestDivisor(nums, threshold):
    low, high = 1, max(nums)
    res = float('inf')

    while low <= high:
        mid = (low + high) // 2
        tot = 0

        for i in nums:
            tot += ceil(i / mid)

        if tot <= threshold:
            res = min(mid, res)
            high = mid - 1
        else:
            low = mid + 1

    return res

nums = list(map(int, input("Enter the array: ").split()))
threshold = int(input("Enter the threshold: "))

print("Smallest divisor:", smallestDivisor(nums, threshold))