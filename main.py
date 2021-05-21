from collections import deque

class MyHashSet:

    '''
    
    U:
    
    mySet = MyHashSet()
    mySet.add(1) {1}
    mySet.add(2) {1, 2}
    mySet.contains(1) True
    mySet.remove(1)
    mySet.contains(1) False
    
    
    
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [None] * 10000
        
        
    def hashIndex(self, key):
        return hash(key) % len(self.arr) # % contains to the length of the array

    def add(self, key: int) -> None:
        hashIndex = self.hashIndex(key)
        if self.arr[hashIndex] == None:
            newList = deque()
            newList.append(key)
            self.arr[hashIndex] = newList
        elif key not in self.arr[hashIndex]:
            self.arr[hashIndex].append(key)
        
    def remove(self, key: int) -> None:
        hashIndex = self.hashIndex(key)
        if self.arr[hashIndex] != None:
            try:
                self.arr[hashIndex].remove(key)
            except:
                pass

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashIndex = self.hashIndex(key)
        if self.arr[hashIndex] != None:
            return key in self.arr[hashIndex]
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)