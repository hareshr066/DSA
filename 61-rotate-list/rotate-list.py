class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # base cases: empty list or nothing to rotate
        if head is None or k == 0:
            return head
        # count the nodes, p stops on the last node
        p = head
        count = 1
        while p.next:
            p = p.next
            count += 1
        # k can be larger than count, so only k % count rotations really matter
        k = k % count
        if k == 0 or k == count:  # a full turn gives the same list
            return head
        # move q to the new tail: the node at position count - k
        q = head
        for i in range(0, (count - k - 1)):
            q = q.next
        # relink the nodes
        p.next = head                   # old tail → old head (makes a circle)
        head = q.next                   # node after the new tail is the new head
        q.next = None                   # cut the circle at the new tail
        return head