package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class No_1865_List {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int tcnum = 0; tcnum < tc; tcnum++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int m = Integer.valueOf(st.nextToken());
            int w = Integer.valueOf(st.nextToken());

            List<int[]> edges = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.valueOf(st.nextToken());
                int e = Integer.valueOf(st.nextToken());
                int t = Integer.valueOf(st.nextToken());
                edges.add(new int[]{s, e, t});
                edges.add(new int[]{e, s, t});
            }

            for (int i = 0; i < w; i++) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.valueOf(st.nextToken());
                int e = Integer.valueOf(st.nextToken());
                int t = Integer.valueOf(st.nextToken());
                edges.add(new int[]{s, e, -t});
            }

            if (bellmanFord(n, edges)) sb.append("YES\n");
            else sb.append("NO\n");
        }
        System.out.print(sb.toString());
    }

    private static boolean bellmanFord(int n, List<int[]> edges) {
        int[] checked = new int[n + 1];
        Arrays.fill(checked, 500 * 10000 + 1);
        for (int i = 0; i < n; i++) {
            for (int[] edge : edges) {
                int s = edge[0];
                int e = edge[1];
                int t = edge[2];
                if (checked[e] <= checked[s] + t) continue;
                checked[e] = checked[s] + t;
                if (i == n - 1) return true;
            }
        }

        return false;
    }
}
