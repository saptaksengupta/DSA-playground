public class ClosestPair {

    public void printClosestPair(int arr1[], int arr2[], int sum) {
        int n = arr1.length;
        int m = arr2.length;

        int i = 0;
        int j = m - 1;

        int diff = 1000000000;
        int resp1 = 0;
        int resp2 = 0;
        while (i < n && j > 0) {
            int currSum = arr1[i] + arr2[j];
            int currDiff = Math.abs(sum - currSum);
            if (currDiff < diff) {
                diff = currDiff;
                resp1 = i;
                resp2 = j;
            }
            if (sum < currSum) {
                j -= 1;
            } else if(sum > currSum) {
                i += 1;
            }
        }

        System.out.println(arr1[resp1] + " " + arr2[resp2]);

    }

    public static void main(String[] args) {
        ClosestPair cp = new ClosestPair();
        int arr1[] = {2, 4, 5, 8};
        int arr2[] = {10, 20, 29, 40};
        int x = 38;
        cp.printClosestPair(arr1, arr2, x);
    }
}