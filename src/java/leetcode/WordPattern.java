import java.util.HashMap;

// Generated By lexicon-dsa CLI tool.
// Author: Saptak Sengupta(deeps.sengupta@gmail.com)
// Github: https://github.com/saptaksengupta/

// Given a pattern and a string s, find if s follows the same pattern.
// Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

// Example 1:
// Input: pattern = "abba", s = "dog cat cat dog"
// Output: true

// Example 2:
// Input: pattern = "abba", s = "dog cat cat fish"
// Output: false

// Example 3:
// Input: pattern = "aaaa", s = "dog cat cat dog"
// Output: false

// Example 4:
// Input: pattern = "abba", s = "dog dog dog dog"
// Output: false

public class WordPattern {

    // Complete the demoFunction function below.
    // You should change the name accordinglly.
    static boolean isMatching(String pattern, String s) {

        HashMap<String, Character> existed = new HashMap<>();
        String sArr[] = s.split(" ");
        if (pattern.length() != sArr.length) {
            return false;
        }
        int i = 0;
        while (i < sArr.length) {
            if (existed.containsKey(sArr[i]) && (existed.get(sArr[i]) != pattern.charAt(i))) {
                return false;
            } else if (!existed.containsKey(sArr[i]) && (existed.containsValue(pattern.charAt(i)))) {
                return false;
            }
            existed.put(sArr[i], pattern.charAt(i));  
            i++;
        }
        return true;
    }

    public static void main(String[] args) {
        String pattern = "abba";
        String s = "dog cat cat fish";
        boolean result = isMatching(pattern, s);
        System.out.println(result);
    }
}