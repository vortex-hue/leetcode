class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        iterate = 0
        for i in range(1, len(nums)):
           if nums[iterate] != nums[i]:
               iterate +=1
               nums[iterate] = nums[i]
        return iterate + 1
