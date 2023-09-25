class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # expectedNums = [x for x in nums if x != val]
        # expectedNums = list(filter(lambda x:x != val, nums))
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index    
            # expectedNums = [x for x in nums if x != val]
        #  k = expectedNums.length
