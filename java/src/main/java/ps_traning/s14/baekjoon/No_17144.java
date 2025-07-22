package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_17144 {

    private static int r, c, t;
    private static int[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.valueOf(st.nextToken());
        c = Integer.valueOf(st.nextToken());
        t = Integer.valueOf(st.nextToken());

        board = new int[r][c];
        List<Integer> airY = new ArrayList<>();
        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < c; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
                if (board[i][j] == -1) airY.add(i);
            }
        }

        for (int i = 0; i < t; i++) {
            spread();
            clear(airY.get(0), new int[]{0, -1, 0, 1}, new int[]{1, 0, -1, 0});
            clear(airY.get(1), new int[]{0, 1, 0, -1}, new int[]{1, 0, -1, 0});
        }

        int answer = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] == -1) continue;
                answer += board[i][j];
            }
        }
        System.out.println(answer);

    }

    private static void clear(int y, int[] dy, int[] dx) {
        Deque<Integer> deque = new ArrayDeque<>();
        int x = 1;
        int d = 0;
        while (board[y][x] != -1) {
            deque.offer(board[y][x]);
            int ny = y + dy[d];
            int nx = x + dx[d];
            if (ny >= r || nx >= c || ny < 0 || nx < 0) d++;
            y = y + dy[d];
            x = x + dx[d];
        }
        deque.pollLast();
        deque.offerFirst(0);

        x = 1;
        d = 0;
        while (board[y][x] != -1) {
            board[y][x] = deque.poll();
            int ny = y + dy[d];
            int nx = x + dx[d];
            if (ny >= r || nx >= c || ny < 0 || nx < 0) d++;
            y = y + dy[d];
            x = x + dx[d];
        }

    }

    private static void spread() {
        int[][] temp = new int[r][c];
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] == 0) continue;
                int w = board[i][j] / 5;
                for (int d = 0; d < 4; d++) {
                    int ay = i + dy[d];
                    int ax = j + dx[d];
                    if (ay >= r || ay < 0 || ax >= c || ax < 0 || board[ay][ax] == -1) continue;
                    temp[ay][ax] += w;
                    board[i][j] -= w;
                }
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                board[i][j] += temp[i][j];
            }
        }
    }
}
