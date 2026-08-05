class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

    # rightMax = -1
    # revere order progression 

        # rightMax = -1 

        # for i in range(len(arr)-1, -1, -1):
        #     newmax   = max(rightMax, arr[i])
        #     arr[i] = rightMax
        #     rightMax = newmax

        # return arr   
        n = len(arr)
        ans = [0]*n  #array of same size

        for i in range(n): #iterating in the original arr of size n 
            rightMax = -1 #initiased with -1 for 
            for j in range(i+1, n):
                rightMax = max(rightMax, arr[j])
            ans[i] = rightMax

        return ans         

        






        