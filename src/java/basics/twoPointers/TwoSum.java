package basics.twoPointers;

public class TwoSum {

    private static boolean isPairMatched(int val, int n, int arr[]) {
        int i = 0;
        int j = n - 1;
        while(i < j) {
            int sum = arr[i] + arr[j];
            if (sum == val) {
                return true;
            } 

            if (sum < val) {
                i+=1;
            } else if (sum > val) {
                j -= 1;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        // it will be sorted array.
        int arr[] = { 3, 5, 9, 2, 8, 10, 11 };  
        int sum = 50;
        System.out.println(isPairMatched(sum, arr.length, arr));
    }
}