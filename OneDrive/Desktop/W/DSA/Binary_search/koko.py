from math import ceil

def find_pile_hour(piles, speed):
    tot_hr = 0

    for pile in piles:
        tot_hr += ceil(pile / speed)

    return tot_hr


def cal(piles, h):
    low = 1
    high = max(piles)

    ans = high

    while low <= high:
        mid = (low + high) // 2

        tot = find_pile_hour(piles, mid)

        if tot <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


piles = list(map(int, input("Enter the array: ").split()))
h = int(input("Enter the total hours: "))

res = cal(piles, h)

print("Minimum eating speed:", res)