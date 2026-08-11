class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #using hashmaps
        res = len(students)
        cnt = Counter(students) #count for every interger in the array

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1 
                cnt[s] -= 1 
            else:
                return res    
        
        return res