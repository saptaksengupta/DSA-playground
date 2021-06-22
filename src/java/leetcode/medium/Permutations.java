// Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

// Example 1:

// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
// Example 2:

// Input: nums = [0,1]
// Output: [[0,1],[1,0]]
// Example 3:

// Input: nums = [1]
// Output: [[1]]

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Permutations {

    public List<List<Integer>> permute(int nums[]) {

        List<List<Integer>> result = new ArrayList<>();
        Boolean[] visited = new Boolean[nums.length];
        Arrays.fill(visited, false);

        permute(nums, result, new ArrayList<>(), visited);

        return result;
    }

    private void permute(int arr[], List<List<Integer>> result, List<Integer> permutation, Boolean[] visited) {
        if (permutation.size() == arr.length) {
            result.add(new ArrayList<>(permutation));
            return;
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println("inside" + permutation.toString() + i);
            if (visited[i]) {
                continue;
            }

            visited[i] = true;
            permutation.add(arr[i]);
            permute(arr, result, permutation, visited);
            visited[i] = false;
            permutation.remove(permutation.size() - 1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int length = Integer.parseInt(sc.nextLine());
        String inputs = sc.nextLine();
        String inputArr[] = inputs.split(" ");
        int numbers[] = new int[length];

        for (int i = 0; i < length; i++) {
            numbers[i] = Integer.parseInt(inputArr[i]);
        }
        Permutations pr = new Permutations();
        List<List<Integer>> result = pr.permute(numbers);

        System.out.println(result);
    }
}