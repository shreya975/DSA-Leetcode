class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):          # first loop
            for j in range(i + 1, len(nums)):  # second loop
                if nums[i] + nums[j] == target:
                    return [i, j]
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        