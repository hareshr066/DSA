class Solution:
    def reverseString(self, s: list[str]) -> None:
        #s.reverse()
        i,j =0,len(s)-1
        while i<j :
            temp = s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1
        """
        Do not return anything, modify s in-place instead.
        """
        