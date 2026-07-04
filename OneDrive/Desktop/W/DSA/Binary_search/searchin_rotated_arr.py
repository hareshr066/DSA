# searching in rotated sorted array - I (unique values only in the array)
def searchI(nums,n,target):
    n= len(nums)
    low,high = 0,n-1
    while low<= high:
        mid = (low+high)//2
        if (nums[mid]==target):
            return mid
        else :
            if nums[low]<=nums[mid]:
                if nums[low]<=target and target<nums[mid]:
                    high=mid-1
                else :
                    low = mid+1
            else :
                if nums[mid]<=target and target<=nums[high]:
                    low=mid+1
                else :
                    high=mid-1
    return -1

# search in a rotated sorted array - II (contains duplicate values)
def searchII(nums,n,target):
    n = len(nums)
    low,high= 0,n-1
    while low <= high :
        mid =(low+high)//2
        if nums[mid]==target:
            return True
        else :
            if nums[low]==nums[mid] and nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            elif nums[low]<=nums[mid]:
                if nums[low]<=target and target<nums[mid]:
                    high=mid-1
                else :
                    low = mid+1
            else :
                if nums[mid]<=target and target<=nums[high]:
                    low=mid+1
                else :
                    high=mid-1
    return False

n  =int(input("Enter the size of the array: "))
target= int(input("Enter the value to search :"))
nums=list(map(int,input("Enter the array :").split()))
I= searchI(nums,n,target)
II=searchII(nums,n,target)
print(I)
print(II)
