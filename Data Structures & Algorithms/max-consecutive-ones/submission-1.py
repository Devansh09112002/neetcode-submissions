class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:



        # n, res  = len(nums) , 0 

        # for i in range(n):
        #     count = 0
        #     for j in  range(i, n):
        #         if nums[j] == 0 : break
        #         count = count +1

        #     res = max (res, count)
        # return res

        res , cnt = 0, 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0: 
                res = max (res , cnt)
                cnt = 0
            else:
                cnt += 1

        return  max(cnt, res)


   



        





        