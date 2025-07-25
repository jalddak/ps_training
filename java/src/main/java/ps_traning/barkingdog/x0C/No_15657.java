package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_15657 {
    private static int n, m;
    private static StringBuilder sb = new StringBuilder();
    private static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        st = new StringTokenizer(br.readLine());
        nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = Integer.valueOf(st.nextToken());
        Arrays.sort(nums);

        back(0, new Stack<>(), 0);
        System.out.print(sb);

    }

    private static void back(int depth, Stack<Integer> result, int start) {
        if (depth == m) {
            for (int num : result) sb.append(num).append(" ");
            sb.append("\n");
            return;
        }

        for (int i = start; i < n; i++) {
            result.push(nums[i]);
            back(depth + 1, result, i);
            result.pop();
        }
    }
}
