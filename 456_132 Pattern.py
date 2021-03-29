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
