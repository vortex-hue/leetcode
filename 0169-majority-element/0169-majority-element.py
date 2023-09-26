import statistics

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        ## using the statistics module prebuilt in python
        data = statistics.mode(nums)
        return data

        