package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class No_5656 {

    private static int n, w, h, answer;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            answer = Integer.MAX_VALUE;
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            int[][] board = new int[h][w];
            for (int i = 0; i < h; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < w; j++) board[i][j] = Integer.parseInt(st.nextToken());
            }

            recursion(0, board);
            if (answer == Integer.MAX_VALUE) answer = 0;
            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.print(sb);
    }

    private static void recursion(int depth, int[][] board) {
        if (depth == n) {
            answer = Math.min(answer, checkBlock(board));
            return;
        }

        for (int x = 0; x < w; x++) {
            if (board[h - 1][x] == 0) continue;

            int[][] copy = new int[h][w];
            for (int i = 0; i < h; i++) System.arraycopy(board[i], 0, copy[i], 0, w);
            breakOut(x, copy);
            fall(copy);
            recursion(depth + 1, copy);
        }
    }

    private static void breakOut(int c, int[][] board) {
        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < h; i++) {
            if (board[i][c] == 0) continue;
            q.add(new int[]{i, c, board[i][c]});
            board[i][c] = 0;
            break;
        }

        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int y = poll[0], x = poll[1], k = poll[2];
            for (int i = 1; i < k; i++) {
                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d] * i;
                    int nx = x + dx[d] * i;
                    if (ny >= h || nx >= w || ny < 0 || nx < 0 || board[ny][nx] == 0) continue;
                    q.offer(new int[]{ny, nx, board[ny][nx]});
                    board[ny][nx] = 0;
                }
            }

        }
    }

    private static void fall(int[][] board) {
        for (int j = 0; j < w; j++) {
            Queue<Integer> q = new ArrayDeque<>();
            for (int i = h - 1; i >= 0; i--) {
                if (q.isEmpty() && board[i][j] != 0) continue;
                if (board[i][j] != 0) {
                    board[q.poll()][j] = board[i][j];
                    board[i][j] = 0;
                }
                if (board[i][j] == 0) q.offer(i);

            }
        }
    }

    private static int checkBlock(int[][] board) {
        int result = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (board[i][j] == 0) continue;
                result++;
            }
        }
        return result;
    }
}

