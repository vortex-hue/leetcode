class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ## setting the iterator to 2
        final = 2

        ## loop to check for the conditions while going through our list
        for i in range(2, len(nums)):
            ## if nums value at index [i ] is not equal to length of nums
            if nums[i] != nums[final-2]:
                
                nums[final] = nums[i]
                final += 1
                ## write extra func for checking if double

        return final 