class Node:

    def __init__(self,key,val):
        self.val = (key,val)
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = {}
        self.cache = Node(0,0)
        self.dummy = self.cache
    
    def move_to_tail(self,key):
        curr  = self.lru_cache[key]
        if curr == self.dummy:
            return
        pre = curr.prev
        nex = curr.next
        pre.next = nex
        if nex:
            nex.prev = pre
        self.dummy.next = curr
        curr.prev = self.dummy
        curr.next = None
        self.dummy = curr
        

    def get(self, key: int) -> int:

        
        if key not in self.lru_cache:
            return -1
        
        self.move_to_tail(key)
        return self.lru_cache[key].val[1]
        
        

    def put(self, key: int, value: int) -> None:

        if key in self.lru_cache:
            curr  = self.lru_cache[key]
            curr.val = (key,value)
            self.move_to_tail(key)
            return 

        if self.capacity == len(self.lru_cache):
            curr = self.cache.next
            if curr:
                self.cache.next = curr.next
                if curr.next:    
                    curr.next.prev = self.cache 
                else:
                    self.dummy = self.cache
                self.lru_cache.pop(curr.val[0])
        
    
        curr = Node(key,value)
        self.lru_cache[key] = curr
        self.dummy.next= curr
        curr.prev = self.dummy
        self.dummy = curr
    
        # print(self.lru_cache)

        
