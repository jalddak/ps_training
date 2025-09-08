package ps_traning.algostudy._250909;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_16118 {

    private static int n, m;
    private static Map<Integer, List<int[]>> edges = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            if (!edges.containsKey(a)) edges.put(a, new ArrayList<>());
            if (!edges.containsKey(b)) edges.put(b, new ArrayList<>());
            edges.get(a).add(new int[]{d, b});
            edges.get(b).add(new int[]{d, a});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return a[0] - b[0];
        });
        double[][] visited = new double[3][n + 1];
        Arrays.fill(visited[0], Integer.MAX_VALUE);
        Arrays.fill(visited[1], Integer.MAX_VALUE);
        Arrays.fill(visited[2], Integer.MAX_VALUE);
        visited[0][1] = 0;
        visited[1][1] = 0;
        // 시간, half, 노드, 상태
        pq.add(new int[]{0, 0, 1, 0});
        pq.add(new int[]{0, 0, 1, 1});

        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int t = poll[0], half = poll[1], node = poll[2], state = poll[3];
            if (visited[state][node] < t + (half == 1 ? 0.5 : 0) || !edges.containsKey(node)) continue;

            for (int[] info : edges.get(node)) {
                int d = info[0], next = info[1];
                int nHalf = half;
                if (state == 1) {
                    if (d % 2 == 1) nHalf++;
                    d /= 2;
                } else if (state == 2) d *= 2;

                int nt = t + d;
                if (nHalf == 2) {
                    nHalf -= 2;
                    nt += 1;
                }
                int nState = state;
                if (nState != 0) nState = nState == 1 ? 2 : 1;
                if (visited[nState][next] <= nt + (nHalf == 1 ? 0.5 : 0)) continue;
                visited[nState][next] = nt + (nHalf == 1 ? 0.5 : 0);
                pq.offer(new int[]{nt, nHalf, next, nState});
            }
        }

        int result = 0;
        for (int i = 0; i <= n; i++) {
            if (visited[0][i] < Math.min(visited[1][i], visited[2][i])) result++;
        }

        System.out.println(result);

    }
}
