class Node:
    def __init__(self, key: int, val:int, next: 'Node' = None, prev: 'Node' = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # hashmap-> key : Node
        self.hashmap = {}

        self.head = Node(0,0,None,None)
        self.tail = Node(0,0,None,self.head)
        self.head.next = self.tail 

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # removefromLL
            node = self.hashmap[key]
            val = node.val
            self.removefromLL(node)
            # addtoLL (adds to front of LL)
            new_node = Node(key,val,None,None)
            self.addtoLL(new_node)

            #hashmap must point to new node created 
            self.hashmap[key] = new_node 
            return val
        else:
            return -1 
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap: 
            # if node alr exist -> remove existing node 
            old_node = self.hashmap[key] 
            self.removefromLL(old_node)
        else: # if node does not exist 
            # if exceed capacity 
            if len(self.hashmap)>=self.capacity:
                # remove LRU node from LL 
                LRU_node = self.tail.prev
                self.removefromLL(LRU_node)
                # remove LRU from hashmap 
                self.hashmap.pop(LRU_node.key)
        # create new node and add to LL 
        new_node = Node(key,value,None,None)
        self.addtoLL(new_node) 
        # create/update key pair in hashmap 
        self.hashmap[key]= new_node
            
        # if key in self.hashmap:
        #     self.removefromLL(self.hashmap[key])
        # elif len(self.hashmap) >= self.capacity:  # only evict if truly new key
        #     end_node = self.tail.prev
        #     self.removefromLL(end_node)
        #     self.hashmap.pop(end_node.key)

        # new_node = Node(key, value, None, None)
        # self.addtoLL(new_node)
        # self.hashmap[key] = new_node


          
    def addtoLL(self,new_node) -> None: 
        #create new node at front of LL 
        next_node = self.head.next 
        self.head.next = new_node 
        new_node.prev = self.head
        new_node.next = next_node 
        next_node.prev = new_node 

    def removefromLL(self,node:Node) -> None: 
        # find node to be removed 
        prev = node.prev
        next_node = node.next

        prev.next = next_node
        next_node.prev = prev 
        

        

        
