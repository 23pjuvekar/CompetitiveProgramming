class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        current_level_head = root

        while current_level_head:
            dummy = Node(0)
            prev = dummy
            cur = current_level_head
            while cur:
                if cur.left:
                    prev.next = cur.left
                    prev = cur.left
                if cur.right:
                    prev.next = cur.right
                    prev = cur.right
                
                cur = cur.next
            
            current_level_head = dummy.next
            
        return root