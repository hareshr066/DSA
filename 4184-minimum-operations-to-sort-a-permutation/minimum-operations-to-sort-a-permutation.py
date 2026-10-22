from typing import List
from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        rev = nums[::-1]
        
      
        
        def find_valid_rotations(arr):
            valid = set()
           
            k = arr.index(0)
            good = True
            for i in range(n):
                if arr[(k + i) % n] != i:
                    good = False
                    break
            if good:
                valid.add(k)
            return valid
        
        valid_nums = find_valid_rotations(nums)
        valid_rev  = find_valid_rotations(rev)
        
        if not valid_nums and not valid_rev:
            return -1
        
        
        pos_in_nums = [0] * n
        pos_in_rev  = [0] * n
        for i, v in enumerate(nums): pos_in_nums[v] = i
        for i, v in enumerate(rev):  pos_in_rev[v]  = i
        
        def get_first_val(is_rev, rot):
            return rev[rot] if is_rev else nums[rot]
        
        def get_last_val(is_rev, rot):
            return rev[(rot + n - 1) % n] if is_rev else nums[(rot + n - 1) % n]
        
        def is_target(is_rev, rot):
            return rot in (valid_rev if is_rev else valid_nums)
        
        start = (False, 0)
        if is_target(*start):
            return 0
        
        visited = {start}
        queue = deque([(False, 0, 0)])
        
        while queue:
            is_rev, rot, ops = queue.popleft()
            
            nr = (rot + 1) % n
            s1 = (is_rev, nr)
            if is_target(*s1): return ops + 1
            if s1 not in visited:
                visited.add(s1)
                queue.append((*s1, ops + 1))
            
           
            last_val = get_last_val(is_rev, rot)
            new_is_rev = not is_rev
            new_rot = pos_in_nums[last_val] if new_is_rev else pos_in_rev[last_val]
            
            new_rot = pos_in_rev[last_val] if new_is_rev else pos_in_nums[last_val]
            s2 = (new_is_rev, new_rot)
            if is_target(*s2): return ops + 1
            if s2 not in visited:
                visited.add(s2)
                queue.append((*s2, ops + 1))
        
        return -1