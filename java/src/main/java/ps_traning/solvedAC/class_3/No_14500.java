package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_14500 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        int[][] board = new int[n][m];
        int maxNum = 0;
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
                maxNum = Math.max(maxNum, board[i][j]);
            }
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Queue<int[]> q = new LinkedList<>();
                q.add(new int[]{board[i][j], i, j, 1, 0});

                List<Integer> candidates = new ArrayList<>();
                while (!q.isEmpty()) {
                    int[] qr = q.poll();
                    int score = qr[0], y = qr[1], x = qr[2], cnt = qr[3], direction = qr[4];

                    if (cnt == 4) {
                        answer = Math.max(answer, score);
                        continue;
                    }

                    if (score + maxNum * (4 - cnt) < answer) continue;

                    for (int d = 0; d < 4; d++) {
                        if (cnt != 1 && direction == (d < 2 ? d + 2 : d - 2)) continue;
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                        q.add(new int[]{score + board[ny][nx], ny, nx, cnt + 1, d});
                        if (cnt == 1) candidates.add(board[ny][nx]);
                    }
                }

                int temp = candidates.stream().mapToInt(Integer::valueOf).sum() + board[i][j];
                if (candidates.size() == 4) temp -= Collections.min(candidates);
                answer = Math.max(answer, temp);
            }
        }

        System.out.println(answer);
    }
}
