# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/

class Solution:

    # Complete the demoFunction function below.
    # You should change the name accordinglly.
    def getFirstUniqueCharIndex(self, str):
        stHash = {}

        for i in range(0, len(str)):
            if str[i] not in stHash:
                stHash.update( {str[i]: {'count': 1, 'index': i} } )
            else: 
                ltCount = stHash.get(str[i])['count'] + 1
                stHash.update({str[i]: {'count': ltCount, 'index': i}})

        for i in stHash:
            if stHash[i]['count'] == 1:
                return stHash[i]['index']
        
        return -1

if __name__ == "__main__":
    testStr = 'loveleetcode'
    instance = Solution()
    print(instance.getFirstUniqueCharIndex(testStr))
