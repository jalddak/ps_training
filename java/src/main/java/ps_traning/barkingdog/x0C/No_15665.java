package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_15665 {

    private static int n, m;
    private static int[] nums;
    private static Stack<Integer> result = new Stack<>();
    private static StringBuilder sb = new StringBuilder();
    private static Set<Integer> set = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) set.add(Integer.valueOf(st.nextToken()));

        nums = set.stream().mapToInt(Integer::valueOf).toArray();
        Arrays.sort(nums);
        recursion(0);
        System.out.print(sb);
    }

    private static void recursion(int depth) {
        if (depth == m) {
            for (int num : result) sb.append(num).append(" ");
            sb.append("\n");
            return;
        }

        for (int num : nums) {
            result.push(num);
            recursion(depth + 1);
            result.pop();
        }
    }
}
