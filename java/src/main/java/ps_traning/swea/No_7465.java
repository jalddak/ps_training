package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_7465 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            List<Integer>[] info = new List[n + 1];
            for (int i = 0; i <= n; i++) {
                info[i] = new ArrayList<>();
            }
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int f = Integer.parseInt(st.nextToken());
                int s = Integer.parseInt(st.nextToken());
                info[f].add(s);
                info[s].add(f);
            }

            int result = 0;
            boolean[] visited = new boolean[n + 1];
            for (int i = 1; i <= n; i++) {
                if (visited[i]) continue;
                visited[i] = true;
                result++;
                Stack<Integer> stack = new Stack<>();
                stack.push(i);
                while (!stack.isEmpty()) {
                    int cur = stack.pop();
                    for (int k : info[cur]) {
                        if (visited[k]) continue;
                        visited[k] = true;
                        stack.push(k);
                    }
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
