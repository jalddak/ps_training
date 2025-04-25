package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_16236 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        int[] shark = new int[4];
        int[][] board = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
                if (board[i][j] == 9) {
                    shark = new int[]{i, j, 2, 0};
                    board[i][j] = 0;
                }
            }
        }

        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        int answer = 0;
        while (true) {
            int sy = shark[0], sx = shark[1], sSize = shark[2], level = shark[3];
            boolean[][] visited = new boolean[n][n];
            visited[sy][sx] = true;

            Queue<int[]> q = new LinkedList<>();
            q.add(new int[]{sy, sx, 0});

            List<int[]> candidates = new ArrayList<>();
            int minTime = n * n;

            while (!q.isEmpty()) {
                int[] qr = q.poll();
                int y = qr[0], x = qr[1], t = qr[2];
                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    int nt = t + 1;
                    if (ny >= n || ny < 0 || nx >= n || nx < 0 || visited[ny][nx] || board[ny][nx] > sSize || nt > minTime)
                        continue;
                    visited[ny][nx] = true;
                    if (board[ny][nx] != 0 && board[ny][nx] < sSize) {
                        candidates.add(new int[]{ny, nx});
                        minTime = Math.min(minTime, nt);
                        continue;
                    }
                    q.offer(new int[]{ny, nx, nt});
                }
            }

            if (candidates.isEmpty()) break;

            answer += minTime;
            candidates.sort(new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1];
                }
            });

            sy = candidates.get(0)[0];
            sx = candidates.get(0)[1];
            board[sy][sx] = 0;
            level++;
            if (level == sSize) {
                level = 0;
                sSize++;
            }
            shark = new int[]{sy, sx, sSize, level};
        }

        System.out.println(answer);
    }

}
