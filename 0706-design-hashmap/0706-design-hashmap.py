class Node:
    def __init__(self,key = -1,value = -1, next = None):
        self.key = key
        self.value = value
        self.next = None
        

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [Node() for _ in range(1000)]
    def _hash(self, key):
        return key % self.size
    def put(self, key: int, value: int) -> None:

        curr = self.buckets[self._hash(key)]

        while curr.next:

            if curr.next.key == key:
                curr.next.value = value
                return 
            curr= curr.next
        curr.next = Node(key,value)
        
        

    def get(self, key: int) -> int:
        
        curr = self.buckets[self._hash(key)].next

        while curr:

            if curr.key == key:
                return curr.value
            curr= curr.next
        return -1
    def remove(self, key: int) -> None:
        
        index = self._hash(key)
        curr = self.buckets[index]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)