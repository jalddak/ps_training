package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2467 {
    private static int n;
    private static int[] nums, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        nums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.valueOf(st.nextToken());
        }

        result = new int[2];

        int l = 0, r = n - 1;
        int minAbsSum = 2 * 1000000000 + 1;
        while (l < r) {
            int sum = nums[l] + nums[r];
            int absSum = Math.abs(sum);
            if (absSum < minAbsSum) {
                minAbsSum = absSum;
                result[0] = nums[l];
                result[1] = nums[r];
            }
            
            if (sum == 0) break;
            else if (sum < 0) l = l + 1;
            else r = r - 1;
        }

        System.out.println(result[0] + " " + result[1]);
    }
}
