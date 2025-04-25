package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class No_1987 {
    private static int r, c, answer;
    private static char[][] board;
    private static int[] dy, dx;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.valueOf(st.nextToken());
        c = Integer.valueOf(st.nextToken());

        board = new char[r][c];
        for (int i = 0; i < r; i++) {
            board[i] = br.readLine().toCharArray();
        }

        dy = new int[]{-1, 0, 1, 0};
        dx = new int[]{0, 1, 0, -1};
        answer = 0;
        dfs(0, 0, new HashSet<>(List.of(board[0][0])));
        System.out.println(answer);
    }

    private static void dfs(int y, int x, Set<Character> s) {
        answer = Math.max(answer, s.size());
        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];
            if (ny >= r || ny < 0 || nx >= c || nx < 0 || s.contains(board[ny][nx])) continue;
            s.add(board[ny][nx]);
            dfs(ny, nx, s);
            s.remove(board[ny][nx]);
        }
    }
}
