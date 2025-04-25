package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_20040 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());

        int[] parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }

        int answer = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.valueOf(st.nextToken());
            int r = Integer.valueOf(st.nextToken());
            int lRoot = find(parents, l);
            int rRoot = find(parents, r);

            if (lRoot == rRoot) {
                answer = i + 1;
                break;
            }

            if (lRoot < rRoot) parents[rRoot] = lRoot;
            else parents[lRoot] = rRoot;

        }

        System.out.println(answer);
    }

    private static int find(int[] parents, int node) {
        return parents[node] == node ? node : find(parents, parents[node]);
    }
}
