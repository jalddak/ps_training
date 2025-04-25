package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1967 {
    private static List<int[]>[] edges;
    private static int[] checked;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        edges = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            edges[i] = new ArrayList<>();
        }
        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int p = Integer.valueOf(st.nextToken());
            int c = Integer.valueOf(st.nextToken());
            int w = Integer.valueOf(st.nextToken());
            edges[p].add(new int[]{c, w});
        }

        checked = new int[n + 1];
        dfs(1);
        int answer = Arrays.stream(checked).max().getAsInt();
        System.out.println(answer);
    }

    private static int dfs(int node) {
        List<Integer> candidates = new ArrayList<>(List.of(0));

        for (int[] edge : edges[node]) {
            int child = edge[0], weight = edge[1];
            if (!edges[child].isEmpty()) weight += dfs(child);
            candidates.add(weight);
        }

        candidates.sort(Comparator.reverseOrder());
        checked[node] = candidates.size() == 1 ? candidates.get(0) : candidates.get(0) + candidates.get(1);
        return candidates.get(0);
    }
}
