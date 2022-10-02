public class TwoSum {

    private static int[] isPairMatched(int target, int n, int nums[]) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++)
        {
            for (int j = 0; j < nums.length; j++)
            {   
                sum = nums[i] + nums[j];
                if (sum == target)
                {
                    return new int[] {i,j};
                }

            }
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        // it will be sorted array.
        int arr[] = { 3, 5, 9, 2, 8, 10, 11 };  
        int sum = 8;
        int[] res = isPairMatched(sum, arr.length, arr);
        if (res.length > 0) {
            System.out.println(res[0] + ", " + res[1]);
        }
    }
}