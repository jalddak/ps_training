package ps_traning.barkingdog.x09;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_16920 {
    private static int n, m, p;
    private static int[] s, answer, dy, dx;
    private static char[][] board;
    private static Queue<int[]>[] qs;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        dy = new int[]{-1, 0, 1, 0};
        dx = new int[]{0, 1, 0, -1};

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        p = Integer.valueOf(st.nextToken());

        s = new int[p + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= p; i++) s[i] = Integer.valueOf(st.nextToken());

        board = new char[n][m];
        qs = new Queue[p + 1];
        for (int i = 1; i <= p; i++) {
            qs[i] = new LinkedList<>();
        }
        answer = new int[p + 1];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                if (!Character.isDigit(board[i][j])) continue;
                int num = board[i][j] - '0';
                answer[num]++;
                qs[num].offer(new int[]{i, j});
            }
        }

        boolean flag = true;
        while (flag) {
            flag = false;
            for (int i = 1; i <= p; i++) {
                Queue<int[]> next = recursion(qs[i], 0, i);
                if (!next.isEmpty()) {
                    qs[i] = next;
                    flag = true;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= p; i++) {
            sb.append(answer[i]).append(" ");
        }
        System.out.println(sb);
    }

    private static Queue<int[]> recursion(Queue<int[]> q, int depth, int num) {
        Queue<int[]> result = new LinkedList<>();
        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int y = poll[0], x = poll[1];
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= n || ny < 0 || nx >= m || nx < 0 || board[ny][nx] != '.') continue;
                board[ny][nx] = (char) (num + '0');
                answer[num]++;
                result.offer(new int[]{ny, nx});
            }
        }
        if (!result.isEmpty() && depth + 1 < s[num]) result = recursion(result, depth + 1, num);
        return result;
    }
}
