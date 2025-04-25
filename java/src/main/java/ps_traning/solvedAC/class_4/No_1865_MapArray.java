package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class No_1865_MapArray {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int tcnum = 0; tcnum < tc; tcnum++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int m = Integer.valueOf(st.nextToken());
            int w = Integer.valueOf(st.nextToken());

            Map<Integer, Integer>[] edges = new HashMap[n + 1];
            for (int i = 0; i <= n; i++) {
                edges[i] = new HashMap<>();
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.valueOf(st.nextToken());
                int e = Integer.valueOf(st.nextToken());
                int t = Integer.valueOf(st.nextToken());
                initEdges(s, e, t, edges);
                initEdges(e, s, t, edges);
            }

            for (int i = 0; i < w; i++) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.valueOf(st.nextToken());
                int e = Integer.valueOf(st.nextToken());
                int t = Integer.valueOf(st.nextToken());
                initEdges(s, e, -t, edges);
            }

            if (bellmanFord(n, edges)) sb.append("YES\n");
            else sb.append("NO\n");
        }
        System.out.print(sb.toString());
    }

    private static void initEdges(int s, int e, int t, Map<Integer, Integer>[] edges) {
        if (!edges[s].containsKey(e) || edges[s].get(e) > t) {
            edges[s].put(e, t);
        }
    }

    private static boolean bellmanFord(int n, Map<Integer, Integer>[] edges) {
        int[] checked = new int[n + 1];
        Arrays.fill(checked, 500 * 10000 + 1);
        for (int i = 0; i < n; i++) {
            for (int s = 0; s < edges.length; s++) {
                if (edges[s].isEmpty()) continue;
                for (int e : edges[s].keySet()) {
                    int t = edges[s].get(e);
                    if (checked[e] <= checked[s] + t) continue;
                    checked[e] = checked[s] + t;
                    if (i == n - 1) return true;
                }
            }
        }

        return false;
    }
}
