class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pos=0
        for i in range(len(nums)) :
            if nums[i]!=0:
                temp=nums[i]
                nums[i]=nums[pos]
                nums[pos]=temp
                pos+=1
        # c=0
        # for i in nums :
        #     if i == 0:
        #         c+=1
        # for i in range(c,len(nums)-1):
        #     nums[i]=0
        
        
        """
        Do not return anything, modify nums in-place instead.
        """
        