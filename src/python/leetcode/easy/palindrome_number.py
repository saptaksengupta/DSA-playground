# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/
import math
class Solution:
    def isPalindrome(self, number):
        if number < 0:
            return False
        
        if number >= 0 and number < 10:
            return True

        if number % 10 == 0: 
            return False
        
        secondHalf = 0
        while secondHalf < number:
            secondHalf = math.floor(number % 10) + (secondHalf * 10)
            number = math.floor(number / 10)
        
        print(number, secondHalf)
        return number == secondHalf or math.floor(secondHalf / 10) == number
        
if __name__ == "__main__":
    instance = Solution()
    print(instance.isPalindrome(121)) 
