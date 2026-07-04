# minimum in rotated sorted array !!
def findMin(nums,n):
    n = len(nums)
    ans=float('inf')
    low,high=0,n-1
    while low <= high :
        mid = (low+high)//2
        if nums[low]<= nums[mid]:
            ans=min(ans,nums[low])
            low=mid+1
        else :
            ans=min(ans,nums[mid])
            high=mid-1
    return ans

n=int(input("Enter the size of the array :"))
nums=list(map(int,input("Enter the values of array:").split()))
ans = findMin(nums,n)
print(ans)

