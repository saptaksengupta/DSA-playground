// Check if given string is Palindrome or not using recursion only.

public class PalindromeString {

    static Boolean isPalindrome(int index, String str, int n) {
        int revIndex = (n - index) - 1;

        if (index >= n / 2) {
            return true;
        }

        if (str.charAt(revIndex) == str.charAt(index)) {
            return isPalindrome(index + 1, str, n);
        }

        return false;
    }

    public static void main(String[] args) {
        String str = "ALO";
        int len = str.length();
        Boolean result = isPalindrome(0, str, len);
        System.out.println(result);
    }
}