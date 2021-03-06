# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/

class Solution:
    def removeElement(self, nums, val: int, matchFound = False)->int:
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1
        
        return count

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    instance = Solution()
    print(instance.removeElement(nums, 2))
