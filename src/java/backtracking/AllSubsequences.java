// Print all sub sequence of a given array
// Example: [1, 3, 2] => [1, 3, 2], [3, 2], [1, 2], [1, 3], [2], [3], [1], []


import java.util.ArrayList;

public class AllSubsequences {

    static void allSubsequences(int index, ArrayList<Integer> ds, int[] arr, int len) {
        if (index == len) {
            System.out.println(ds);
            return;
        }

        ds.add(arr[index]);
        allSubsequences(index + 1, ds, arr, len);
        ds.remove(ds.size() - 1);
        allSubsequences(index + 1, ds, arr, len);
    }

    public static void main(String[] args) {
        int arr[] = {1, 3, 2};
        int length = arr.length;
        ArrayList<Integer> list = new ArrayList<>();
        allSubsequences(0, list, arr, length);
    }
}