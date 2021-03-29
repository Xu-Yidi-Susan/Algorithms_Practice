# Sliding Window Maximum
Actually, the first version I wrote failed to pass the leetcode test, as the running time exceeded the limit. A clever way to solve this problem is using a **deque(double-ended queue)**. The key insight is that the deque always matains a list of candidate maximum in monotonically decreasing order.

## Reasoning Process
Using a deque to keep the index of the elements that might be the maximum in the sliding window.
1. If the deque is empty, then put the index *i* of the new element into the deque.
2. If the deque is not empty, the tail element in the deque is index *j*, if array[j] >= array[i], then put the index *i* of the new element in the deque. Otherwise, we need to repeat popping out the tail element until the deque is empty or array[j] >= array[i], then put the index *i* in the deque.
3. If the index *i* - the head element in the deque == the length of sliding window, pop out the head element.

## Flowchart
![avatar](https://www.geekxh.com/assets/img/4.f3a9aa62.jpg)

## Code 
This version I wrote might not look very concise.
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = []
        max_list = []
        sub_nums_start = 0
        idx = 0

        while sub_nums_start <= len(nums)-1:
            if len(deque) == 0:
                deque.append(sub_nums_start)
            else:
                if nums[sub_nums_start] <= nums[deque[-1]]:
                    deque.append(sub_nums_start)
                else:
                    for i in range(0, len(deque)):
                        if nums[deque[-1]] < nums[sub_nums_start]:
                            deque.pop()
                    deque.append(sub_nums_start)
                
            sub_nums_start += 1
            idx += 1
            
            if deque[-1] - deque[0] >= k:
                deque.pop(0)

            if idx >= k:
                max_list.append(nums[deque[0]])
        return max_list
```
A standard version
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # write code here
        # 存放可能是最大值的下标
        maxqueue = []
        # 存放窗口中最大值
        maxlist = []
        n = len(nums)
        # 参数检验
        if n == 0 or k == 0 or k > n:
            return maxlist
        for i in range(n):
            # 判断队首下标对应的元素是否已经滑出窗口
            if len(maxqueue) > 0 and i - k >= maxqueue[0]:
                maxqueue.pop(0)
            while len(maxqueue) > 0 and nums[i] > nums[maxqueue[-1]]:
                maxqueue.pop()
            maxqueue.append(i)
            if i >= k - 1:
                maxlist.append(nums[maxqueue[0]])
        return maxlist
```
## Reference
[Sliding window minimum/maximum algorithm](https://www.nayuki.io/page/sliding-window-minimum-maximum-algorithm)

