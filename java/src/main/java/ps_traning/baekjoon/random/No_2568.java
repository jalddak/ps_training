package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_2568 {

    private static int n;
    private static int[][] edges;
    private static List<List<int[]>> arr = new ArrayList<>();
    private static Set<Integer> candidates = new HashSet<>();

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());

        edges = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            edges[i][0] = Integer.valueOf(st.nextToken());
            edges[i][1] = Integer.valueOf(st.nextToken());
        }

        Arrays.sort(edges, (a, b) -> Integer.compare(a[0], b[0]));
        binarySearch();

        int before = arr.get(arr.size() - 1).get(arr.get(arr.size() - 1).size() - 1)[0];
        for (int i = arr.size() - 1; i >= 0; i--) {
            for (int j = arr.get(i).size() - 1; j >= 0; j--) {
                int temp = arr.get(i).get(j)[0];
                if (before < temp) continue;
                candidates.add(temp);
                before = temp;
                break;
            }
        }

        StringBuilder sb = new StringBuilder();
        System.out.println(n - candidates.size());
        for (int i = 0; i < n; i++) {
            if (candidates.contains(edges[i][0])) continue;
            sb.append(edges[i][0]).append("\n");
        }
        System.out.print(sb);
    }

    private static void binarySearch() {
        for (int i = 0; i < n; i++) {
            int l = -1, r = arr.size();
            while (l + 1 < r) {
                int mid = (l + r) / 2;
                if (arr.get(mid).get(arr.get(mid).size() - 1)[1] >= edges[i][1]) r = mid;
                else l = mid;
            }
            if (r == arr.size()) {
                arr.add(new ArrayList<>());
                arr.get(r).add(edges[i]);
                continue;
            }
            arr.get(r).add(edges[i]);
        }
    }
}
