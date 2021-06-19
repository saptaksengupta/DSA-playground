// Given a string s, find the length of the longest substring without repeating characters.

// Example 1:
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.

// Example 2:
// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.

// Example 3:
// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

// Example 4:
// Input: s = ""
// Output: 0


public class LnSubStrWoutRpt {

    static int getLength(String s) {
        String existed = "";
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            int indexOfChar = existed.indexOf(s.charAt(i));
            existed += s.charAt(i);
            if (indexOfChar > -1) { // exited char
                existed = existed.substring(indexOfChar + 1);  
            } 
            
            if (existed.length() > maxLength) {
                maxLength = existed.length();
            }
        }

        return maxLength;
    }

    public static void main(String[] args) {
        String s = "aabaab!bb";
        // String s = "abcaabcd";
        int result = getLength(s);
        System.out.println(result);
    }
}