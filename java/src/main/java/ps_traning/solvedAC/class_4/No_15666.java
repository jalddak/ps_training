package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_15666 {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static StringBuilder sb;
    private static int n, m;
    private static List<Integer> nums;


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        st = new StringTokenizer(br.readLine());
        Set<Integer> set = new HashSet<>();
        while (st.hasMoreTokens()) {
            set.add(Integer.valueOf(st.nextToken()));
        }
        nums = new ArrayList<>(set);
        nums.sort(Integer::compareTo);
        n = nums.size();
        sb = new StringBuilder();
        recursion(0, 0, new Stack<>());
        System.out.print(sb.toString());
    }

    private static void recursion(int depth, int start, Stack<Integer> result) {
        if (depth == m) {
            for (int num : result) sb.append(num).append(" ");
            sb.append("\n");
            return;
        }

        for (int i = start; i < n; i++) {
            result.push(nums.get(i));
            recursion(depth + 1, i, result);
            result.pop();
        }
    }
}
