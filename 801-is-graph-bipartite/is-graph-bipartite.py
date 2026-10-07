from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        # # using Bfs
        # def bfs(start):
        #     q = deque()
        #     q.append(start)
        #     coloured[start]=0
        #     while q :
        #         node = q.popleft()
        #         for nei in graph[node]:
        #             if coloured[nei] == -1:
        #                 coloured[nei]=1-coloured[node]
        #                 q.append(nei)
        #             if coloured[nei]==coloured[node]:
        #                 return False
        #     return True
        # coloured = [-1]*len(graph)
        # for i in range(len(graph)):
        #     if coloured[i]==-1:
        #         if not bfs(i):
        #             return False 
        # return True
        # using DFS 
        colored = [-1]*len(graph)
        def dfs(node) :
            for nei in graph[node]:
                if colored[nei]==-1:
                    colored[nei]=1-colored[node]
                    if not dfs(nei):
                        return False
                if colored[node]==colored[nei]:
                    return False
            return True
        for i in range(len(graph)):
            if colored[i]==-1:
                if not dfs(i):
                    return False
        return True
        
               
                        


        