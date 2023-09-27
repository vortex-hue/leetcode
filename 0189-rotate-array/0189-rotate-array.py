class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)  ## The int for slicing the list
        nums[:] = nums[-k:] + nums[:-k] ## modifies the original list itself
        print(nums) ##printing to stdout for test purposes
        return nums
       
        