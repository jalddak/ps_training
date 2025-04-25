package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_11725 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        List<Integer>[] edges = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            edges[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());

            edges[s].add(e);
            edges[e].add(s);
        }

        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[n + 1];
        int[] answer = new int[n + 1];
        q.add(1);
        visited[1] = true;

        while (!q.isEmpty()) {
            int node = q.poll();
            for (int nextNode : edges[node]) {
                if (visited[nextNode]) continue;
                visited[nextNode] = true;
                q.add(nextNode);
                answer[nextNode] = node;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 2; i <= n; i++) {
            sb.append(answer[i]).append("\n");
        }
        System.out.print(sb.toString());
    }
}
