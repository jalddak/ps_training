package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_2638 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());

        int[][] board = new int[n][m];
        boolean[][] visited = new boolean[n][m];
        int[][] checked = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
            }
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        pq.offer(new int[]{0, 0, 0});
        visited[0][0] = true;

        int[] dy = new int[]{-1, 0, 1, 0};
        int[] dx = new int[]{0, 1, 0, -1};

        int answer = 0;
        while (!pq.isEmpty()) {
            int[] pqr = pq.poll();
            int t = pqr[0], y = pqr[1], x = pqr[2];
            answer = Math.max(t, answer);
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                int nt = t;
                if (ny >= n || ny < 0 || nx >= m || nx < 0 || visited[ny][nx]) continue;
                if (board[ny][nx] == 1) {
                    checked[ny][nx]++;
                    if (checked[ny][nx] < 2) continue;
                    nt++;
                }
                visited[ny][nx] = true;
                pq.offer(new int[]{nt, ny, nx});
            }
        }

        System.out.println(answer);
    }
}
