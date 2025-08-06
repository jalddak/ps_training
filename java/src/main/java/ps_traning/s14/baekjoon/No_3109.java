package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_3109 {

    private static int r, c;
    private static char[][] board;
    private static boolean[][] visited;
    private static int[] dy = {-1, 0, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        board = new char[r][c];
        visited = new boolean[r][c];
        for (int i = 0; i < r; i++) {
            board[i] = br.readLine().toCharArray();
        }

        int cnt = 0;
        for (int i = 0; i < r; i++) {
            if (recursion(i, 0)) cnt++;
        }
        System.out.println(cnt);
    }

    private static boolean recursion(int y, int x) {
        boolean result = false;
        if (x == c - 1) return true;
        for (int d = 0; d < 3; d++) {
            int ny = y + dy[d];
            int nx = x + 1;
            if (ny >= r || nx >= c || ny < 0 || nx < 0 || board[ny][nx] == 'x' || visited[ny][nx]) continue;

            board[ny][nx] = 'x';
            result = recursion(ny, nx);
            if (result) break;
            visited[ny][nx] = true;
            board[ny][nx] = '.';
        }
        return result;
    }
}