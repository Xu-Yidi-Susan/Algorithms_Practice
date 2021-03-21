class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A = sum(A)
        sum_B = sum(B)
        sum_mean = (sum(A) + sum(B))/2
        diff_A = sum_mean - sum_A
        for i in range(0, len(A)):
            if A[i] + diff_A in B:
                ex_A = A[i]
                ex_B = B[B.index(A[i] + diff_A)]
                return [ex_A, ex_B]
