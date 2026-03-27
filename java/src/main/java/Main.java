import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    private static char[] arr;
    private static int n;
    private static char[] cd = {'1', '2', '3'};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new char[n];

        recursion(0);
        System.out.println(String.valueOf(arr));
    }

    private static boolean recursion(int depth) {
        if (!check(depth))
            return false;
        if (depth == n)
            return true;

        for (char num : cd) {
            arr[depth] = num;
            boolean result = recursion(depth + 1);
            if (!result) continue;
            return result;
        }
        return false;
    }

    private static boolean check(int depth) {
        boolean result = true;
        int half = depth / 2;
        for (int i = 1; i <= half; i++) {
            result = false;
            for (int j = 0; j < i; j++) {
                if (arr[depth - 1 - j] != arr[depth - 1 - i - j]) {
                    result = true;
                    break;
                }
            }
            if (!result) break;
        }
        return result;
    }
}