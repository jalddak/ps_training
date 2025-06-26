package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_15663 {
    private static int n, m;
    private static int[] nums;
    private static StringBuilder sb = new StringBuilder();
    private static Stack<Integer> result = new Stack<>();
    private static Map<Integer, Integer> check = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.valueOf(st.nextToken());
            check.put(num, check.containsKey(num) ? check.get(num) + 1 : 1);
        }

        n = check.size();
        nums = check.keySet().stream().mapToInt(Integer::valueOf).toArray();
        back(0);
        System.out.print(sb);
    }

    private static void back(int depth) {
        if (depth == m) {
            for (int num : result) sb.append(num).append(" ");
            sb.append("\n");
            return;
        }

        for (int i = 0; i < n; i++) {
            if (check.get(nums[i]) == 0) continue;
            check.put(nums[i], check.get(nums[i]) - 1);
            result.push(nums[i]);
            back(depth + 1);
            result.pop();
            check.put(nums[i], check.get(nums[i]) + 1);
        }
    }
}
