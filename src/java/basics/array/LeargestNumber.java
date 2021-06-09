import java.util.Arrays;
import java.util.Comparator;

// Problem Statement: 

// Given a list of non negative integers, arrange them in such a manner 
// that they form the largest number possible.
// The result is going to be very large, 
// hence return the result in the form of a string.

public class LeargestNumber {

    static String getLeargestNumber(int arr[]) {
        
        if (arr.length == 0) {
            return "";
        }

        String sortedSting[] = new String[arr.length];
        for (int i = 0; i < sortedSting.length; i++) {
            sortedSting[i] = Integer.toString(arr[i]);
        }

        Arrays.sort(sortedSting, new Comparator<String>(){
            public int compare(String a, String b) {
                String ab = a + b;
                String ba = b + a;

                return ba.compareTo(ab);
            } 
        });

        if (sortedSting[0].equals("0")) {
            return "0";
        }

        StringBuilder sb = new StringBuilder();
        for (String s: sortedSting) {
            sb.append(s);
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        int arr[] = {3, 30, 34, 5, 9};
        String result = getLeargestNumber(arr);
        System.out.println(result);
    }
}