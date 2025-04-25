package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1238 {
    private static int n, m, x;
    private static Map<Integer, Map<Integer, Integer>> edges, reverseEdges;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        x = Integer.valueOf(st.nextToken());

        edges = new HashMap<>();
        reverseEdges = new HashMap<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());
            int t = Integer.valueOf(st.nextToken());
            checkEdges(s, e, t, edges);
            checkEdges(e, s, t, reverseEdges);
        }

        int[] result1 = checkMinTime(edges);
        int[] result2 = checkMinTime(reverseEdges);

        int answer = 0;
        for (int i = 1; i <= n; i++) {
            answer = Math.max(answer, result1[i] + result2[i]);
        }
        System.out.println(answer);

    }

    private static void checkEdges(int s, int e, int t, Map<Integer, Map<Integer, Integer>> edges) {
        if (!edges.containsKey(s)) {
            Map<Integer, Integer> endTime = new HashMap<>();
            endTime.put(e, t);
            edges.put(s, endTime);
        } else if (!edges.get(s).containsKey(e) || edges.get(s).get(e) > t) {
            edges.get(s).put(e, t);
        }
    }

    private static int[] checkMinTime(Map<Integer, Map<Integer, Integer>> edges) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        pq.offer(new int[]{0, x});
        int[] result = new int[n + 1];
        Arrays.fill(result, 1000 * 100 + 1);
        result[x] = 0;

        while (!pq.isEmpty()) {
            int[] pqr = pq.poll();
            int t = pqr[0], l = pqr[1];
            if (result[l] < t) continue;

            for (int nl : edges.get(l).keySet()) {
                int nt = t + edges.get(l).get(nl);
                if (result[nl] <= nt) continue;
                result[nl] = nt;
                pq.offer(new int[]{nt, nl});
            }
        }
        return result;
    }
}
