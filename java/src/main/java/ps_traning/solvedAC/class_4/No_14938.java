package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_14938 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        int r = Integer.valueOf(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] t = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            t[i] = Integer.valueOf(st.nextToken());
        }

        int[][] edges = new int[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                edges[i][j] = 16;
                if (i == j) edges[i][j] = 0;
            }
        }
        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());
            int distance = Integer.valueOf(st.nextToken());
            if (edges[s][e] <= distance) continue;
            edges[s][e] = distance;
            edges[e][s] = distance;
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    edges[i][j] = Math.min(edges[i][j], edges[i][k] + edges[k][j]);
                }
            }
        }

        int answer = 0;
        for (int i = 1; i <= n; i++) {
            int temp = 0;
            for (int j = 1; j <= n; j++) {
                if (edges[i][j] > m) continue;
                temp += t[j];
            }
            answer = Math.max(answer, temp);
        }
        System.out.println(answer);
    }
}
