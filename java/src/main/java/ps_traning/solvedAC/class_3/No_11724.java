package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_11724 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        boolean[] visited = new boolean[n + 1];
        List<List<Integer>> vs = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            vs.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.valueOf(st.nextToken());
            int v2 = Integer.valueOf(st.nextToken());
            vs.get(v1).add(v2);
            vs.get(v2).add(v1);
        }

        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            answer++;
            Queue<Integer> q = new LinkedList<>();
            q.offer(i);
            while (!q.isEmpty()) {
                int x = q.poll();
                for (int v : vs.get(x)) {
                    if (visited[v]) continue;
                    visited[v] = true;
                    q.offer(v);
                }
            }
        }

        System.out.println(answer);
    }
}
