package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_14621_kruskal {

    private static int n, m, answer, count;
    private static char[] g;
    private static int[] p;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        g = new char[n];
        p = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            g[i] = Character.valueOf(st.nextToken().charAt(0));
            p[i] = i;
        }

        answer = 0;
        count = 0;

        List<int[]> infos = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int f = Integer.parseInt(st.nextToken()) - 1;
            int s = Integer.parseInt(st.nextToken()) - 1;
            int cost = Integer.parseInt(st.nextToken());

            if (g[f] == g[s]) {
                continue;
            }

            infos.add(new int[]{f, s, cost});
        }
        infos.sort((a, b) -> a[2] - b[2]);
        for (int[] info : infos) {
            union(info);
            if (count == n - 1) break;
        }

        System.out.println(count == n - 1 ? answer : -1);
    }

    private static void union(int[] info) {
        int a = info[0], b = info[1], cost = info[2];
        int pa = find(a);
        int pb = find(b);
        if (pa != pb) {
            p[pb] = pa;
            answer += cost;
            count += 1;
        }
    }

    public static int find(int x) {
        if (p[x] == x) {
            return x;
        }
        return p[x] = find(p[x]);
    }
}
