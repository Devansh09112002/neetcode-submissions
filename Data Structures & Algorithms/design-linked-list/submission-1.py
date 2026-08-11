class ListNode:
    # DLL
    # def __init__(self ,  val):  
    #     self.val = val
    #     self.next = None 
    #     self.prev = None

    #SLL
    def __init__(self ,  val):  
        self.val = val
        self.next = None 

class MyLinkedList:
    #DLL
    # def __init__(self):
    #     self.left = ListNode(0)
    #     self.right = ListNode(0)
    #     self.left.next = self.right
    #     self.right.prev = self.left
    #SLL
    def __init__(self):
        self.left = ListNode(0)
        
    #DLL
    # def get(self, index: int) -> int:

    #     cur = self.left.next
    #     while cur and index >0:
    #         cur = cur.next 
    #         index -= 1
    #     if cur and cur != self.right and index == 0:
    #         return cur.val
    #     return -1    
    #SLL
    def get(self, index: int) -> int:

        cur = self.left.next
        while cur and index > 0:
            cur = cur.next 
            index -= 1
        if cur  and index == 0:
            return cur.val
        return -1
    
    #DLL
    # def addAtHead(self, val: int) -> None:

    #     node, next , prev = ListNode(val), self.left.next , self.left
    #     prev.next = node 
    #     next.prev = node 
    #     node.next = next 
    #     node.prev = prev
    #SLL
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.left.next
        self.left.next = node 

    #DLL
    # def addAtTail(self, val: int) -> None:

    #     node, next , prev = ListNode(val), self.right , self.right.prev
    #     prev.next = node 
    #     next.prev = node 
    #     node.next = next 
    #     node.prev = prev
    #SLL
    def addAtTail(self, val: int) -> None:
        cur = self.left

        while cur.next:
            cur = cur.next

        node = ListNode(val)    
        cur.next = node       
        
    # #DLL
    # def addAtIndex(self, index: int, val: int) -> None:
    #     cur = self.left.next
    #     while cur and index > 0:
    #         cur = cur.next 
    #         index -= 1
    #     if cur and index == 0:
    #         node = ListNode(val)

    #SLL          
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left
        while cur and index > 0:
            cur = cur.next 
            index -= 1
        if cur and index == 0:
            node = ListNode(val)
            node.next = cur.next
            cur.next = node


    #DLL
    # def deleteAtIndex(self, index: int) -> None:

    #     cur = self.left.next
    #     while cur and index >0:
    #         cur = cur.next 
    #         index -= 1
    #     if cur and cur != self.right and  index == 0:
    #         next , prev = cur.next , cur.prev
    #         next.prev = prev
    #         prev.next = next

    #SLL 
    def deleteAtIndex(self, index: int) -> None:

        cur = self.left
        while cur and index >0:
            cur = cur.next 
            index -= 1
        if cur and cur.next and  index == 0:
            cur.next = cur.next.next      

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)