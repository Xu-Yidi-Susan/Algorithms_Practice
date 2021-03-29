# 132 Pattern
1. 使用单调栈维护3
    - 遍历的位置*j*相当于132模式中的3，即nums[j]
    - 找到3左边的**最小元素**为1，即nums[i]
    - 找到3右边**比3小的最大元素**2，即nums[k]

2. 132模式中2具有的特性
    - 比3小
    - 在nums[j+1, N-1]中的最大值
    - →使用单调递减的栈，最大元素在栈底，次大元素在栈底的第二元素
    
3. 模拟过程：
从后向前扫描的过程中，一旦当前元素nums[i]比栈顶大，这个nums[i]或许就是所要找的nums[j]，弹出栈中所有比它小的元素，最后一个弹出的就是符合条件的最大nums[k]，如果这个nums[k]比继续向前扫描到的nums[i]大，则符合条件。

![avatar](https://thumbsnap.com/i/juDsnG9Y.png)

```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        numsk = float("-inf")

        for i in range(len(nums)-1,-1,-1):
            if stack == []:
                stack.append(nums[i])
                continue
            
            if nums[i] < numsk:
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    numsk = stack.pop()
                stack.append(nums[i])
        
        return False
```
