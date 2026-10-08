class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        V = numCourses
        graph = [[] for _ in range(V)]
        for u, v in prerequisites:
            graph[v].append(u)
        visited = [False] * V
        pathvis = [False] * V
        order = []
        def dfs(node):
            visited[node] = True
            pathvis[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    if dfs(nei):
                        return True
                elif pathvis[nei]:
                    return True
            pathvis[node] = False
            order.append(node)
            return False
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return []
        order.reverse()
        return order