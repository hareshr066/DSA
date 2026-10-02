class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def back(opc,clc):
            if len(stack)==n*2:
                res.append("".join(stack))
                return
            if opc<n:
                stack.append("(")
                back(opc+1,clc)
                stack.pop()
            if clc<opc:
                stack.append(")")
                back(opc,clc+1)
                stack.pop()
        back(0,0)
        return res 
            
            