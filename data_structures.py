
class LinkedList(): #ListNode
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        
        head = self
        ans = ''
        while head:
            ans += str(head.val) + ' '
            head = head.next
        return ans
    
    
class BinaryTree(): #TreeNode
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
    
class Stack():
    def __init__(self) -> None:
        self.stack = []
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        
    def push(self, item):
        self.stack.append(item)
        
    def __str__(self) -> str:
        return ' '.join([str(i) for i in self.stack])
    
a = [1,2,3]
import random
random.choice(a)