from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        start = "0000"
        if start in deadends:
            return -1
        if start == target:
            return 0
        queue = deque([start])
        visited = {start}
        steps = 0
        while queue:
            # Number of states at the current BFS level
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                for i in range(4):
                    digits = list(node)
                    digit = int(node[i])
                    up = (digit + 1) % 10
                    down = (digit - 1) % 10
                    # +1 move
                    digits[i] = str(up)
                    nei = "".join(digits)
                    if nei not in deadends and nei not in visited:
                        if nei == target:
                            return steps + 1
                        visited.add(nei)
                        queue.append(nei)
                    # -1 move
                    digits[i] = str(down)
                    nei = "".join(digits)
                    if nei not in deadends and nei not in visited:
                        if nei == target:
                            return steps + 1
                        visited.add(nei)
                        queue.append(nei)
            steps += 1
        return -1