# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        ss=[]
        a = list1
        while a:
            ss.append(a.val)
            a=a.next
        b = list2
        while b :
            ss.append(b.val)
            b=b.next
        ss.sort()
        node = ListNode(0)
        temp = node 
        for x in ss:
            temp.next=ListNode(x)
            temp=temp.next
        return node.next

        

        
        