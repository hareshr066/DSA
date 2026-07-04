# this is using the lowerbound and upperbound concept :
def firstt(nums,n,target):
    low =0
    first=len(nums)
    n= len(nums)
    high=n-1
    while low<= high:
        mid = (low+high)//2
        if nums[mid]>=target:
            first=mid
            high=mid-1
        else :
            low=mid+1
    return first
def lastt(nums,n,target):
    low = 0
    last=len(nums)
    n =len(nums)
    high=n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>target:
            last=mid
            high=mid-1
        else :
            low=mid+1
    return last
n = int(input("Enter the length of the array :"))
nums=list(map(int,input("Enter the values of the array :").split()))
target = int(input("Enter the target :"))
lb = firstt(nums,n,target)
ub = lastt(nums,n,target)
if lb==len(nums) or nums[lb]!= target:
    print([-1,-1])
else :
    print(lb,ub-1)

