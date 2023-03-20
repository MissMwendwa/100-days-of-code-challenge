# in this solution, I will use to approaches to solving this two sum leetcode problem

# define the class
class Solution:

    #define the data method
    def two_sum(self, nums =List[int], target =int) -> List[int]:

        #declare the hashmap
        hashmap = {}

        # define the decision loop
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            tar_2 = target - nums[i]

            # check validity
            if tar_2 in hashmap and hashmap[tar_2] != i:
                return [i, hashmap[tar_2]]