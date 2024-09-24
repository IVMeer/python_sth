n = 6
path = [' '] * n
print("first:",path)

ans = []
ans.append(''.join(path))

print("second:", ans)

class ListCode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        dummy = head