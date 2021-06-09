// Calculate power of x over N.
// in O(logN) time conplexity.

public class PowerCalc {

    static int calculate(int x, int n) {
        if (n == 0) {
            return 1; 
        }

        if (n == 1) {
            return x;
        }

        int temp = calculate(x, n / 2);

        if (n % 2 == 0) {
            return temp * temp;
        } else {
            return x * temp * temp;
        }
    }

    public static void main(String[] args) {
        int result = calculate(2, 3);
        System.out.println("Result: " + result);
    }
}