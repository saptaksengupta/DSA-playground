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

    public static void main(String[] args) {
        int arr[] = {1, 3, 2};
        int sum = 0;
        printSubSequences(0, new ArrayList<Integer>(), sum, arr);
    }
}