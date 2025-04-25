package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class No_11054 {
    private static int n;
    private static int[] nums, rNums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        nums = new int[n];
        rNums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.valueOf(st.nextToken());
            nums[i] = num;
            rNums[n - i - 1] = num;
        }

        List<Integer>[] dp = new ArrayList[2];
        for (int i = 0; i < 2; i++) {
            dp[i] = new ArrayList<>();
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            bs(-1, dp[0].size(), dp[0], nums[i]);
            bs(-1, dp[1].size(), dp[1], rNums[i]);
            result[i] += dp[0].size();
            result[n - i - 1] += dp[1].size();
        }

        int answer = Arrays.stream(result).max().getAsInt() - 1;
        System.out.println(answer);
    }

    private static void bs(int l, int r, List<Integer> list, int num) {
        while (l + 1 < r) {
            int mid = (l + r) / 2;
            if (check(list, num, mid)) r = mid;
            else l = mid;
        }
        if (r == list.size()) list.add(num);
        else list.set(r, num);
    }

    private static boolean check(List<Integer> list, int num, int index) {
        return list.get(index) >= num;
    }
}
