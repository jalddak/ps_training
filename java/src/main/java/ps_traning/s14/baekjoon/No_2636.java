package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_2636 {


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        int[][] board = new int[n][m];
        boolean[][] visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Queue<int[]> cur = new ArrayDeque<>();
        cur.offer(new int[]{0, 0});
        visited[0][0] = true;

        int time = 0;
        int before = 0;
        while (true) {
            Queue<int[]> next = new ArrayDeque<>();
            while (!cur.isEmpty()) {
                int[] poll = cur.poll();
                int y = poll[0], x = poll[1];
                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    if (ny >= n || nx >= m || ny < 0 || nx < 0 || visited[ny][nx]) continue;
                    if (board[ny][nx] == 0) cur.offer(new int[]{ny, nx});
                    else next.offer(new int[]{ny, nx});
                    visited[ny][nx] = true;
                }
            }
            int cnt = next.size();
            if (cnt == 0) break;
            before = cnt;
            cur = next;
            time++;
        }

        System.out.println(time);
        System.out.println(before);
    }
}