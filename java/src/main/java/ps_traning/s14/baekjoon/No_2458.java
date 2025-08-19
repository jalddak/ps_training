package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2458 {

    private static int n, m;
    private static boolean[][] boardChild;
    private static boolean[][] boardParent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        boardChild = new boolean[n + 1][n + 1];
        boardParent = new boolean[n + 1][n + 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            boardChild[a][b] = true;
            boardParent[b][a] = true;
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (boardChild[i][k] && boardChild[k][j]) {
                        boardChild[i][j] = true;
                    }
                    if (boardParent[i][k] && boardParent[k][j]) {
                        boardParent[i][j] = true;
                    }
                }
            }
        }

        int result = 0;
        for (int i = 1; i <= n; i++) {
            int cnt = 0;
            for (int j = 1; j <= n; j++) {
                if (boardChild[i][j]) cnt += 1;
                if (boardParent[i][j]) cnt += 1;
            }
            if (cnt == n - 1) result++;
        }
        System.out.println(result);
    }
}