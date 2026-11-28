class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        temp = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next 
        # Attach whichever list still has nodes
        temp.next = list1 or list2
        return dummy.next