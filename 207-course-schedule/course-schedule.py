class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # premap =[[] for _ in range(numCourses)]
        # visited = set()
        # for course,pre in prerequisites :
        #     premap[course].append(pre)
        # def dfs(course):
        #     if premap[course]==[]:
        #         return True
        #     if course in visited:
        #         return False 
        #     visited.add(course)
        #     for pre in premap[course]:
        #         if not dfs(pre):
        #             return False
        #     visited.remove(course)
        #     premap[course]=[]
        #     return True
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True
        V = numCourses
        graph =[[] for _ in range(V)]
        for u,v in prerequisites:
            graph[v].append(u)
        visited=[False]*V
        pathvis=[False]*V
        def dfs(node):
            visited[node]=True
            pathvis[node]=True
            for nei in graph[node]:
                # if not visited
                if not visited[nei]:
                    if dfs(nei):
                        return True
                # already visited
                elif pathvis[nei]:
                    return True
            pathvis[node]=False
            return False
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return False
        return True

        