class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
        def dfs(node, target):
            if node == target:
                return True
            for nei in graph[node]:
                if dfs(nei, target):
                    return True
            return False
        res = []
        for u, v in queries:
            res.append(dfs(u, v))
        return res