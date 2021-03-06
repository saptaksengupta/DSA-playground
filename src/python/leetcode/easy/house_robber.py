# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/

class Solution:

    # Complete the demoFunction function below.
    # You should change the name accordinglly.
    def rob(self, nums):
        numberOfHouses = len(nums)

        if numberOfHouses == 1:
            return nums[0]
        elif numberOfHouses == 2: 
            return max(nums[0], nums[1])

        d = {0: nums[0], 1: max(nums[0], nums[1])}

        for i in range(2, numberOfHouses):
            d[i] = max(d[i - 1], nums[i] + d[i-2])

        return d[numberOfHouses - 1]

if __name__ == "__main__":
    inputs =[2,7,9,3,1]
    instance = Solution()
    print(instance.rob(inputs))
