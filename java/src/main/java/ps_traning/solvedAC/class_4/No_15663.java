package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_15663 {
    private static int n, m;
    private static BufferedReader br;
    private static StringTokenizer st;
    private static Map<Integer, Integer> ncnts;
    private static StringBuilder sb;
    private static List<Integer> nums;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        ncnts = new HashMap<>();
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int num = Integer.valueOf(st.nextToken());
            int cnt = ncnts.containsKey(num) ? ncnts.get(num) + 1 : 1;
            ncnts.put(num, cnt);
        }

        nums = new ArrayList<>(ncnts.keySet());
        sb = new StringBuilder();
        recursion(0, new Stack<>());

        System.out.print(sb.toString());

    }

    private static void recursion(int depth, Stack<Integer> result) {
        if (depth == m) {
            for (int num : result) sb.append(num).append(" ");
            sb.append("\n");
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            if (ncnts.get(num) < 1) continue;
            ncnts.replace(num, ncnts.get(num) - 1);
            result.push(num);
            recursion(depth + 1, result);
            result.pop();
            ncnts.replace(num, ncnts.get(num) + 1);
        }
    }
}
