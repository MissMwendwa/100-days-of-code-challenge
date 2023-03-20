# in this particular solution, I'll just be using the loop
class Solution:

    #define the data method
    def two_sum(self, nums =List[int], target =int) -> List[int]:

        # start the loop
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return[i, j]