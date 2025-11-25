package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_1167 {

    private static int n, result;
    private static List<int[]>[] info;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        info = new List[n + 1];
        for (int i = 1; i <= n; i++) info[i] = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int node = Integer.parseInt(st.nextToken());
            while (true) {
                int child = Integer.parseInt(st.nextToken());
                if (child == -1) break;
                int d = Integer.parseInt(st.nextToken());
                info[node].add(new int[]{child, d});
            }
        }

        result = 0;
        boolean[] visited = new boolean[n + 1];
        visited[1] = true;
        recursion(1, visited);

        System.out.println(result);

    }

    private static int recursion(int node, boolean[] visited) {
        int first = 0;
        int second = 0;

        for (int[] arr : info[node]) {
            int child = arr[0];
            if (visited[child]) continue;
            visited[child] = true;
            int d = arr[1];
            int t = recursion(child, visited) + d;
            second = Math.max(second, t);
            if (first < second) {
                int temp = first;
                first = second;
                second = temp;
            }
        }

        result = Math.max(result, first + second);
        return first;
    }
}
