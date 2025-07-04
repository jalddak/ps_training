package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_15664 {

    private static int n, m;
    private static int[] nums;
    private static Stack<Integer> result = new Stack<>();
    private static StringBuilder sb = new StringBuilder();
    private static Map<Integer, Integer> info = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.valueOf(st.nextToken());
            info.put(num, info.containsKey(num) ? info.get(num) + 1 : 1);
        }

        nums = info.keySet().stream().mapToInt(Integer::valueOf).toArray();
        Arrays.sort(nums);
        n = nums.length;

        recursion(0, 0);
        System.out.print(sb);
    }

    private static void recursion(int depth, int start) {
        if (depth == m) {
            for (int num : result) sb.append(num).append(" ");
            sb.append("\n");
            return;
        }

        for (int i = start; i < n; i++) {
            int num = nums[i];
            if (info.get(num) == 0) continue;
            info.put(num, info.get(num) - 1);
            result.push(num);
            recursion(depth + 1, i);
            result.pop();
            info.put(num, info.get(num) + 1);
        }
    }
}
