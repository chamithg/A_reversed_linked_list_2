# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dh = ListNode()
        dh.next = head
        runner = dh
        dh2 = ListNode()
        runner2 = dh2
        runner3 = dh2
        position = 0

        while runner:
            if position < left:
                runner2.next = ListNode(runner.val)
                runner2 = runner2.next
                runner3 = runner3.next 
            elif position >= left and position <= right:               
                temp = runner3.next
                runner3.next = ListNode(runner.val)
                if temp:
                    runner3.next.next = temp
                while runner2.next:
                    runner2 = runner2.next    
            elif position > right:
                runner2.next = ListNode(runner.val)
                runner2 = runner2.next
            runner = runner.next
            position +=1


        return dh2.next.next