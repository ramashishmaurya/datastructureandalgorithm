class Solution(object):
    def topKFrequent(self, nums, k):

        result = {}

        for num in nums :
            result[num] = 1 + result.get(num , 0 )

        sorted_nums = sorted(result, key=result.get, reverse=True)

        return sorted_nums[:k]