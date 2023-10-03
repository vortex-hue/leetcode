class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        ## looping through the list
        for i in range(1,len(nums)):
           output.append(output[i-1] + nums[i])
           
        ## return the output of the loop
        return output
        print(output)  # This will print [1,3,4,5]