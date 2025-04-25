package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_1167 {
    private static List<int[]>[] edges;
    private static boolean[] visited;
    private static int[] result;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int v = Integer.valueOf(br.readLine());

        edges = new ArrayList[v + 1];
        for (int i = 0; i < v; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            edges[n] = new ArrayList<>();
            while (true) {
                int linkedNode = Integer.valueOf(st.nextToken());
                if (linkedNode == -1) break;
                int distance = Integer.valueOf(st.nextToken());
                edges[n].add(new int[]{linkedNode, distance});
            }
        }

        visited = new boolean[v + 1];
        result = new int[v + 1];
        visited[1] = true;
        dfs(1);
        System.out.println(Arrays.stream(result).max().getAsInt());
    }

    private static int dfs(int node) {
        List<Integer> candidates = new ArrayList<>();
        candidates.add(0);

        for (int[] edge : edges[node]) {
            int child = edge[0], distance = edge[1];
            if (visited[child]) continue;
            visited[child] = true;
            candidates.add(dfs(child) + distance);
        }

        candidates.sort(Comparator.reverseOrder());
        result[node] = candidates.size() > 1 ? candidates.get(0) + candidates.get(1) : candidates.get(0);
        return candidates.get(0);
    }
}
