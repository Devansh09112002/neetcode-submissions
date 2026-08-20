class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force approach 

        # for mat in range(len(matrix)):
        #     for val in  range(len(matrix[0])):
        #         if matrix[mat][val] == target:
        #             return True
        # return False  

        #most optimized 

        Rows , Cols = len(matrix) , len(matrix[0])
        top , bot = 0 , Rows - 1

        while top <= bot:
            midrow = (top+bot)//2
            if target > matrix[midrow][-1]: #last value of that row
                top = midrow + 1 
            elif target < matrix[midrow][0]: #less than first value of mdirow
                bot = midrow - 1
            else:
                break  #the number might be in the midrow itself so check

        if not (top <= bot):   
            return False

        l , r = 0 , Cols - 1  #create two pointers to tell first and last value 
        midrow = (top+bot)//2  #again define it bcz previous one was inside the fnc not global

        while l <= r:
            midval = (l+r)//2
            if target > matrix[midrow][midval]:
                l = midval+1

            elif target < matrix[midrow][midval]:
                r = midval -1
            else:
                return True

        return False               














        


        