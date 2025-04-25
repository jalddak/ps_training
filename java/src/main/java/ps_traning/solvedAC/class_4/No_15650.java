package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_15650 {
    private static int n, m;
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());

        recursion(0, new Stack<>(), 1);
        System.out.print(sb.toString());
    }

    private static void recursion(int depth, Stack<Integer> result, int start) {
        if (depth == m) {
            for (int num : result) sb.append(num).append(" ");
            sb.append("\n");
        }

        for (int i = start; i <= n; i++) {
            result.add(i);
            recursion(depth + 1, result, i + 1);
            result.pop();
        }
    }
}
