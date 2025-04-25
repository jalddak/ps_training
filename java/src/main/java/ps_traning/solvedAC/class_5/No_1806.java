package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1806 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());

        int[] nums = new int[n];
        int[] sums = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.valueOf(st.nextToken());
            sums[i + 1] = sums[i] + nums[i];
        }

        int l = 0, r = 1;
        int minLen = n + 1;
        while (r <= n && l != r && minLen > 1) {
            if (sums[r] - sums[l] >= m) {
                minLen = Math.min(minLen, r - l);
                l += 1;
            } else r += 1;
        }

        int answer = minLen != n + 1 ? minLen : 0;
        System.out.println(answer);
    }
}
