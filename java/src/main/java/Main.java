import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    private static int r, c, answer;
    private static char[][] board;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};
    private static Set<Character> set = new HashSet<>();

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        answer = 0;

        board = new char[r][c];

        for (int i = 0; i < r; i++) {
            board[i] = br.readLine().toCharArray();
        }

        set.add(board[0][0]);
        dfs(1, 0, 0);

        System.out.println(answer);
    }

    private static void dfs(int depth, int y, int x) {

        answer = Math.max(depth, answer);
        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];

            if (ny < 0 || nx < 0 || ny >= r || nx >= c || set.contains(board[ny][nx])) continue;
            set.add(board[ny][nx]);
            dfs(depth + 1, ny, nx);
            set.remove(board[ny][nx]);
        }
    }
}