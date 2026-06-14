# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        i = 0
        main =  head 
        n = 0
        while main :
            n += 1
            main = main.next

        main = head
        finale = -float("inf")
        ans = []
        while main :
            if i <= (n//2-1) :
                ans.append(main.val)
            else :
                finale = max(finale , main.val + ans.pop())
            i += 1
            main = main.next
        
        return finale
        