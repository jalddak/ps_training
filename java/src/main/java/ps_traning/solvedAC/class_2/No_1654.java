package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] kn = new int[2];
        int i = 0;
        while (st.hasMoreTokens()) kn[i++] = Integer.valueOf(st.nextToken());
        long[] nums = new long[kn[0]];
        for (i = 0; i < kn[0]; i++) {
            nums[i] = Long.valueOf(br.readLine());
        }
        long[] candidate = binarySearch(nums, kn[1]);

        long answer;
        if (getCnt(nums, candidate[1]) >= kn[1]) answer = candidate[1];
        else answer = candidate[0];

        System.out.println(answer);
    }

    public static long[] binarySearch(long[] nums, int n) {
        long left = 1;
        long right = Arrays.stream(nums).max().getAsLong();
        while (left + 1 < right) {
            long middle = (left + right) / 2;
            int cnt = getCnt(nums, middle);
            if (cnt >= n) left = middle;
            else right = middle - 1;
        }
        return new long[]{left, right};
    }

    private static int getCnt(long[] nums, long middle) {
        int cnt = 0;
        for (long num : nums) cnt += num / middle;
        return cnt;
    }


}
