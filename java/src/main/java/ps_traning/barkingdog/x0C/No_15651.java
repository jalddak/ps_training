package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_15651 {
    private static int n, m;
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());

        back(0, new Stack<>());
        System.out.print(sb);
    }

    private static void back(int depth, Stack<Integer> result) {
        if (depth == m) {
            for (int num : result) sb.append(num).append(" ");
            sb.append("\n");
            return;
        }

        for (int i = 1; i <= n; i++) {
            result.push(i);
            back(depth + 1, result);
            result.pop();
        }
    }
}
