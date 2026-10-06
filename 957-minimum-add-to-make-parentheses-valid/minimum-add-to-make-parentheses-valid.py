class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        isvalid = False 
        opened=0
        closed=0
        stack =[]
        for i in s :
            if stack and stack[-1]=="(" and i==")":
                stack.pop()
            else :
                stack.append(i)
        return len(stack)
        # for i in s :
        #     if i=="(":
        #         opened+=1
        #     if i==")":
        #         closed+=1
        # minc=float('inf')
        # c=0
        # while not isvalid:
        #     if opened==closed:
        #         isvalid=True
        #     if opened<closed:
        #         opened+=1
        #         c+=1
        #     else :
        #         closed+=1
        #         c+=1
        #     # minc=min(minc,)
        # return c-1
            
        