from collections import deque
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        # using Bfs
        def bfs(start):
            q = deque()
            q.append(start)
            coloured[start]=0
            while q :
                node = q.popleft()
                for nei in graph[node]:
                    if coloured[nei] == -1:
                        coloured[nei]=1-coloured[node]
                        q.append(nei)
                    if coloured[nei]==coloured[node]:
                        return False
            return True
        coloured = [-1]*len(graph)
        for i in range(len(graph)):
            if coloured[i]==-1:
                if not bfs(i):
                    return False 
        return True
                
                        


        