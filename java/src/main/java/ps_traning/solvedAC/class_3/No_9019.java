package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_9019 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.valueOf(br.readLine());
        char[] dslr = {'D', 'S', 'L', 'R'};

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());

            boolean[] visited = new boolean[10000];
            String[] cmds = new String[10000];
            Queue<Integer> q = new LinkedList<>();
            visited[s] = true;
            cmds[s] = "";
            q.add(s);


            loop:
            while (!q.isEmpty()) {
                int n = q.poll();
                List<Integer> candidates = new ArrayList<>();
                candidates.add(n * 2 < 10000 ? n * 2 : n * 2 % 10000);
                candidates.add(n - 1 < 0 ? 9999 : n - 1);
                candidates.add(n / 1000 + n % 1000 * 10);
                candidates.add(n / 10 + n % 10 * 1000);

                for (int d = 0; d < 4; d++) {
                    int cn = candidates.get(d);
                    if (visited[cn]) continue;
                    visited[cn] = true;
                    cmds[cn] = cmds[n] + dslr[d];
                    q.add(cn);
                    if (cn == e) {
                        sb.append(cmds[cn]).append("\n");
                        break loop;
                    }
                }
            }
        }

        System.out.print(sb.toString());

    }
}
