class Solution(object):
    def majorityElement(self, nums):

        hashmap = {}

        for i in nums : 
            hashmap[i] = 1 + hashmap.get(i , 0)
        
        for num in hashmap :
            if hashmap[num] > len(nums) // 2 : 
                return num 
                