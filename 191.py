class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = []
        divisor = 2**31
        for i in range(0,32):
            x = n//divisor
            temp.append(x)
            n = n - x*divisor
            divisor = divisor/2
        return temp.count(1)
