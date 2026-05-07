# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        now = head
        
        while now.next:
            cnt += 1
            now = now.next
        
        ans = head
        for i in range(cnt//2):
            ans = ans.next
        
        return ans            
            
            
        
        