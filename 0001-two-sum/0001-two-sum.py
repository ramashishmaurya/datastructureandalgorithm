class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i , values in enumerate(nums):

            targetvalues = target - values 

            if targetvalues in hashmap :

                return (hashmap[targetvalues] , i )
                
            hashmap[values] = i 
        
