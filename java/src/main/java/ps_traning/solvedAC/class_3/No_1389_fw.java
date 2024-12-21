package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 플로이드 워셜
public class No_1389_fw {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());

        int[][] board = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            Arrays.fill(board[i], (int) 101);
            board[i][0] = 0;
            board[i][i] = 0;
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.valueOf(st.nextToken());
            int n2 = Integer.valueOf(st.nextToken());
            board[n1][n2] = 1;
            board[n2][n1] = 1;
        }

        for (int k = 1; k <= n; k++) {
            for (int a = 1; a <= n; a++) {
                for (int b = 1; b <= n; b++) {
                    board[a][b] = Math.min(board[a][b], board[a][k] + board[k][b]);
                }
            }
        }

        int answer = 0;
        int cnt = 10000;
        for (int i = 1; i <= n; i++) {
            int temp = Arrays.stream(board[i]).sum();
            if (temp < cnt) {
                answer = i;
                cnt = temp;
            }
        }

        System.out.println(answer);
    }
}
