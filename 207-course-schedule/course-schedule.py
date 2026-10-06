class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        premap = [[] for _ in range(numCourses)]
        for course,pre in prerequisites:
            premap[course].append(pre)
        visited=set()
        def dfs(course):
            if premap[course] == []:
                return True
            if course in visited :
                return False
            visited.add(course)
            for pre in premap[course]:
                if not dfs(pre) :
                    return False
            visited.remove(course)
            premap[course]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False 
        return True

        