
// Count number of subsets, having sum is = k.

public class SubsetSum {

    static int getSubsetCount(int index, int sum, int arr[], int length) {
        if (sum == 0) {
            return 1;
        }

        if (index == length) {
            if (sum == 0) {
                return 1;
            }

            return 0;
        }

        int lCount = 0;
        int rCount = 0;
        if (arr[index] <= sum) {
            lCount = getSubsetCount(index, sum - arr[index], arr, length);
        }
        rCount = getSubsetCount(index + 1, sum, arr, length);

        return lCount + rCount;
    }

    public static void main(String[] args) {
        int arr[] = {1, 3, 2};
        int sum = 4;
        int result = getSubsetCount(0, sum, arr, arr.length);
        System.out.println("Subset Count is: " + result);
    }
}