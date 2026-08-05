class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

    # rightMax = -1
    # revere order progression 

        rightMax = -1 

        for i in range(len(arr)-1, -1, -1):
            newmax   = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newmax

        return arr   
        






        