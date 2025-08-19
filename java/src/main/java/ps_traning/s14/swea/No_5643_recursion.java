package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

class No_5643_recursion {

    private static int n, m;
    private static Set<Integer>[] parents;
    private static Set<Integer>[] childs;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tcCnt = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.parseInt(br.readLine());
            int m = Integer.parseInt(br.readLine());

            parents = new Set[n + 1];
            childs = new Set[n + 1];
            for (int i = 1; i <= n; i++) {
                parents[i] = new HashSet<>();
                childs[i] = new HashSet<>();
            }
            for (int i = 0; i < m; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                parents[b].add(a);
                childs[a].add(b);
            }

            boolean[] visited = new boolean[n + 1];
            for (int i = 1; i <= n; i++) {
                recursion(i, childs, visited);
            }
            visited = new boolean[n + 1];
            for (int i = 1; i <= n; i++) {
                recursion(i, parents, visited);
            }

            int result = 0;
            for (int i = 1; i <= n; i++) {
                if (parents[i].size() + childs[i].size() != n - 1) continue;
                result++;
            }

            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static void recursion(int node, Set<Integer>[] set, boolean[] visited) {
        Set<Integer> nodes = new HashSet<>();
        for (int next : set[node]) {
            if (!visited[next]) recursion(next, set, visited);
            nodes.addAll(set[next]);
        }
        set[node].addAll(nodes);
        visited[node] = true;
    }
}
