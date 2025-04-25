package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_17144 {
    private static int r, c, t;
    private static int[][] board;
    private static int[] dy, dx;
    private static List<Integer> cleaner = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.valueOf(st.nextToken());
        c = Integer.valueOf(st.nextToken());
        t = Integer.valueOf(st.nextToken());

        board = new int[r][c];
        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < c; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
                if (board[i][j] == -1) cleaner.add(i);
            }
        }

        dy = new int[]{-1, 0, 1, 0};
        dx = new int[]{0, 1, 0, -1};

        for (int i = 0; i < t; i++) {
            spread();
            clean();
        }

        int answer = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] > 0) answer += board[i][j];
            }
        }
        System.out.println(answer);
    }

    private static void spread() {
        int[][] temp = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] <= 0) continue;
                int amount = board[i][j] / 5;
                for (int d = 0; d < 4; d++) {
                    int ny = i + dy[d];
                    int nx = j + dx[d];
                    if (ny >= r || ny < 0 || nx >= c || nx < 0 || board[ny][nx] < 0) continue;
                    temp[ny][nx] += amount;
                    board[i][j] -= amount;
                }
            }
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                board[i][j] += temp[i][j];
            }
        }
    }

    private static void clean() {
        for (int i = cleaner.get(0) - 1; i > 0; i--) {
            board[i][0] = board[i - 1][0];
        }
        for (int i = 0; i < c - 1; i++) {
            board[0][i] = board[0][i + 1];
        }
        for (int i = 0; i < cleaner.get(0); i++) {
            board[i][c - 1] = board[i + 1][c - 1];
        }
        for (int i = c - 1; i > 1; i--) {
            board[cleaner.get(0)][i] = board[cleaner.get(0)][i - 1];
        }

        board[cleaner.get(0)][1] = 0;

        for (int i = cleaner.get(1) + 1; i < r - 1; i++) {
            board[i][0] = board[i + 1][0];
        }
        for (int i = 0; i < c - 1; i++) {
            board[r - 1][i] = board[r - 1][i + 1];
        }
        for (int i = r - 1; i > cleaner.get(1); i--) {
            board[i][c - 1] = board[i - 1][c - 1];
        }
        for (int i = c - 1; i > 1; i--) {
            board[cleaner.get(1)][i] = board[cleaner.get(1)][i - 1];
        }

        board[cleaner.get(1)][1] = 0;
    }
}
