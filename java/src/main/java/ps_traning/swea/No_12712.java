package ps_traning.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 누적합으로 풀면 더 효율적으로 자원을 사용할 것 같지만, 오히려 코드가 길어지고 복잡해져서 코테에 쓸모가 없음.
 */
public class No_12712 {

    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int m = Integer.valueOf(st.nextToken());
            int[][] board = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) board[i][j] = Integer.valueOf(st.nextToken());
            }

            int answer = solution(n, m, board);
            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.print(sb);
    }

    private static int solution(int n, int m, int[][] board) {
        int result = 0;
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                int temp1 = spread(n, m, board, y, x, new int[]{-1, 0, 1, 0}, new int[]{0, 1, 0, -1});
                int temp2 = spread(n, m, board, y, x, new int[]{-1, -1, 1, 1}, new int[]{-1, 1, 1, -1});
                result = Math.max(result, Math.max(temp1, temp2));
            }
        }
        return result;
    }

    private static int spread(int n, int m, int[][] board, int y, int x, int[] dy, int[] dx) {
        int result = board[y][x];
        for (int d = 0; d < 4; d++) {
            for (int i = 1; i < m; i++) {
                int ty = y + dy[d] * i;
                int tx = x + dx[d] * i;
                if (ty < 0 || tx < 0 || ty >= n || tx >= n) continue;
                result += board[ty][tx];
            }
        }
        return result;
    }
}
