# Linked list example

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def get_data(self):
        return self.val
    
    def set_data(self, val):
        self.val = val
        
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
        
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0
        
    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
        
    def find(self, val):
        #TODO: find the first item with a given value
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        
        return None
    
    def delete_at(self, idx):
        #TODO: delete an item at given index
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
            
            
            
