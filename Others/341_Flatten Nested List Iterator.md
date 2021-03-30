## 一、递归：构造函数中提前扁平化整个嵌套列表
遍历输入的嵌套列表的所有元素，判断每个元素是int还是list
 1. 如果当前元素是int，放入队列尾部
 2. 如果当前元素是list，则对当前子list继续递归
```python
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
```

## 二、迭代：调用hasNext()或next()方法时扁平化当前嵌套的子列表
1. 在构造函数中应该初始化，把当前列表的各个元素(`不用摊平`)`逆序`放入栈中
2. 在hasNext()中，访问(`不弹出`)栈顶元素，判断是否为int
   - 如果是int，则说明有下一个元素，返回True；然后next()会被调用，弹出栈顶的int
   - 如果是list，则把当前列表的各个元素(`不用摊平`)`逆序`放入栈中
   - 如果栈为空，说明原始的嵌套列表已经访问结束，返回False
 
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
