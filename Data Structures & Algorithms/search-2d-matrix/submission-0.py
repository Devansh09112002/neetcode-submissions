class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute 
        for mat in range(len(matrix)):
            for val in  range(len(matrix[0])):
                if matrix[mat][val] == target:
                    return True
        return False             

        


        