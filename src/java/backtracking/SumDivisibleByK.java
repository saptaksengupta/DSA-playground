import java.util.ArrayList;

// Print all Sub Sequences of an array having sum divisible by K

public class SumDivisibleByK {

    // Complete the demoFunction function below.
    // You should change the name accordinglly.
    static void printSubSequences(int index, ArrayList<Integer> ds, int sum, int[] arr) {

        if (index == arr.length){
            if (sum % 2 == 0 && ds.size() > 0) {
                System.out.println(ds);
            } 
            return;
        }

        ds.add(arr[index]);
        printSubSequences(index + 1, ds, sum + arr[index], arr);

        ds.remove(ds.size() - 1);
        printSubSequences(index + 1, ds, sum, arr);
    }

    /**
     * @param int index: currentIndex
     * @param int sum: currentSum
     * @param int arr: givenArray
     * @return int count of subsequences who's sum is divisible by k.
     */
    static int getCountDivisibleByK(int index, int sum, int[] arr) {
        
        if (index == arr.length) {
            if (sum % 2 == 0){
                return 1;
            }
            return 0;
        }
        int l = getCountDivisibleByK(index + 1, sum + arr[index], arr);
        int r = getCountDivisibleByK(index + 1, sum, arr);

        return (l + r);
    }

    public static void main(String[] args) {
        int arr[] = {1, 3, 2};
        int sum = 0;
        printSubSequences(0, new ArrayList<Integer>(), sum, arr);
        int countWithEmptySet = getCountDivisibleByK(0, sum, arr);
        System.out.println("count is: " + (countWithEmptySet - 1));
    }
}