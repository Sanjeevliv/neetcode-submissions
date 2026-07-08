# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
    
        node = head
        list = []
        maxsum = 0
        while node:
            list.append(node.val)
            node = node.next
        
        n = len(list)
        for i in range(n):
            maxsum = max(maxsum, list[i] + list[n-1-i])
        return maxsum
