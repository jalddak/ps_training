package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1197 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.valueOf(st.nextToken());
        int e = Integer.valueOf(st.nextToken());

        List<int[]>[] edges = new ArrayList[v + 1];
        for (int i = 0; i <= v; i++) {
            edges[i] = new ArrayList<>();
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.valueOf(st.nextToken());
            int b = Integer.valueOf(st.nextToken());
            int c = Integer.valueOf(st.nextToken());
            edges[a].add(new int[]{b, c});
            edges[b].add(new int[]{a, c});
        }

        boolean[] visited = new boolean[v + 1];
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        pq.add(new int[]{0, 1});

        int answer = 0;
        while (!pq.isEmpty()) {
            int[] pqr = pq.poll();
            int cost = pqr[0], node = pqr[1];
            if (visited[node]) continue;
            visited[node] = true;
            answer += cost;
            for (int[] temp : edges[node]) {
                int nNode = temp[0], nCost = temp[1];
                if (visited[nNode]) continue;
                pq.add(new int[]{nCost, nNode});
            }
        }

        System.out.println(answer);
    }
}
