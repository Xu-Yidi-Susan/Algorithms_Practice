# Flatten Nested List Iterator

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []
        self.take_out(nestedList)
   
    def take_out(self, array):
        for item in array:
            if item.isInteger():
                self.queue.append(item.getInteger())
            else:
                self.take_out(item.getList())
 
    def next(self) -> int:
        return self.queue.pop(0)

    def hasNext(self) -> bool:
        if len(self.queue) > 0:
            return True
       

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```
```python
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for item in nestedList:
            self.stack.append(item)
        
    def next(self) -> int:
        return self.stack.pop(0).getInteger()
    
    def hasNext(self) -> bool:
        if (len(self.stack)) <= 0:
            return False
        else:
            if self.stack[0].isInteger():
                return True
            else:
                while self.stack[0].isInteger() is not True:
                    temp = self.stack.pop(0).getList()
                    for item in temp[::-1]:
                        self.stack.insert(0,item)
                    if len(self.stack) == 0:
                        return False
                return True
```














