package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1220 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= 10; tc++) {
            sb.append("#").append(tc).append(" ");
            int len = Integer.valueOf(br.readLine());
            int[][] board = new int[len][len];

            for (int i = 0; i < len; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < len; j++) {
                    board[i][j] = Integer.valueOf(st.nextToken());
                }
            }

            int result = 0;
            for (int i = 0; i < len; i++) {
                boolean flag = false;
                int cur = -1;
                int cnt = 0;
                for (int j = 0; j < len; j++) {
                    if (!flag && (board[j][i] == 0 || board[j][i] == 2)) continue;
                    flag = true;
                    if (board[j][i] == 0 || board[j][i] == cur) continue;
                    cur = board[j][i];
                    if (cur == 2) cnt++;
                }
                result += cnt;
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
