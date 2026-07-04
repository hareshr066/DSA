# this is based on the normal binary search approach !!
def firstt(nums,n,target):
    low =0
    first=-1
    n= len(nums)
    high=n-1
    while low<= high:
        mid = (low+high)//2
        if nums[mid]==target:
            first=mid
            high=mid-1
        elif nums[mid]>target :
            high=mid-1
        else :
            low=mid+1
    return first
def lastt(nums,n,target):
    low = 0
    last=-1
    n =len(nums)
    high=n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            last=mid
            low=mid+1
        elif nums[mid]>target:
            high=mid-1
        else :
            low=mid+1
    return last
n = int(input("Enter the length of the array :"))
nums=list(map(int,input("Enter the values of the array :").split()))
target = int(input("Enter the target :"))
print(firstt(nums,n,target),lastt(nums,n,target))

