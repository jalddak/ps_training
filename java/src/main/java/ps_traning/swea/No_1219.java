package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_1219 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;
        for (int tc = 1; tc <= tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int trash = Integer.valueOf(st.nextToken());
            int length = Integer.valueOf(st.nextToken());

            sb.append("#").append(tc).append(" ");
            st = new StringTokenizer(br.readLine());

            List<Integer>[] edges = new ArrayList[100];
            for (int i = 0; i < 100; i++) {
                edges[i] = new ArrayList<>();
            }

            for (int i = 0; i < length * 2; i += 2) {
                int s = Integer.valueOf(st.nextToken());
                int e = Integer.valueOf(st.nextToken());
                edges[s].add(e);
            }

            Stack<Integer> stack = new Stack<>();
            stack.push(0);
            boolean[] visited = new boolean[100];
            visited[0] = true;

            int result = 0;
            while (!stack.isEmpty()) {
                int cur = stack.pop();

                if (cur == 99) {
                    result = 1;
                    break;
                }

                for (int next : edges[cur]) {
                    if (visited[next]) continue;
                    visited[next] = true;
                    stack.push(next);
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
