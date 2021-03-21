class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        col = [i for i in range(0, len(matrix[0]))]
        idx = 0
        exp = []
        
        for i in range(0, len(matrix)):
            if matrix[i].count(0) > idx:
                temp = []
                for j in col:
                    if matrix[i][j] == 0:
                        temp.append(j)
                        for m in range(i+1, len(matrix)):
                            if matrix[m][j] == 0:
                                exp.append(m)
                        for n in range(0, len(matrix)):
                            matrix[n][j] = 0
                        idx += 1
                matrix[i] = [0 for i in range(0, len(matrix[0]))]
                for x in temp:
                    col.remove(x)
        
        for i in exp:
            matrix[i] = [0 for i in range(0, len(matrix[0]))]
        
        return matrix
            
                            
        
                
                    
