# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/


class Solution:

    # Complete the demoFunction function below.
    # You should change the name accordinglly.
    def lengthOfLongestSubstring(self, s):

        existedList = []
        maxLen = 0
        if len(s) == 1:
            return 1

        for i in s:
            if i in existedList:
                existedList = existedList[existedList.index(i) + 1:]
            existedList.append(i)
            maxLen = max(maxLen, len(existedList))
        return maxLen

    


if __name__ == "__main__":

    inputStr = input('Enter String: ')

    instance = Solution()
    result = instance.lengthOfLongestSubstring(inputStr)
    print(result)

