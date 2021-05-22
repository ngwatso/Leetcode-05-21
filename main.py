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

# ===============

def csAverageOfTopFive(scores):
    
    import math
    
    students = {}

    results = []

    for i in scores:
        if i[0] not in students:
            students[i[0]] = []
        students[i[0]].append(i[1])

    for s in students:
        s = students[s].sort()
        
    for j in students:
        if len(students[j]) > 5:
            students[j] = students[j][-5:]
            
    for t in students:
        students[t] = math.floor(sum(students[t])/len(students[t]))
        
    for key, value in students.items():
        results.append([key, value])
        
    return results

    # ===============

    def csMaxNumberOfLambdas(text):

    myStr = "lambda"

    counts = {}

    for i in myStr:
        if i in text:
            counts[i] =+ text.count(i)
        print('counts', counts)
        
    if counts["l"] == counts["a"]/2 and counts["l"] == counts["m"] and counts["l"] == counts["b"] and counts["l"] == counts["d"]:
        
        return counts["l"]
        
    else:
        return 0