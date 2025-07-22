package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class No_1873 {

    private static int h, w, y, x;
    private static char[][] board;
    private static int[] dy = {-1, 1, 0, 0};
    private static int[] dx = {0, 0, -1, 1};
    private static StringBuilder sb = new StringBuilder();
    private static Map<Character, Integer> cmdDir = new HashMap<>();
    private static Map<Character, Integer> tankDir = new HashMap<>();
    private static Map<Integer, Character> tankDir2 = new HashMap<>();

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.valueOf(br.readLine());

        cmdDir.put('U', 0);
        cmdDir.put('D', 1);
        cmdDir.put('L', 2);
        cmdDir.put('R', 3);

        tankDir.put('^', 0);
        tankDir.put('v', 1);
        tankDir.put('<', 2);
        tankDir.put('>', 3);


        tankDir2.put(0, '^');
        tankDir2.put(1, 'v');
        tankDir2.put(2, '<');
        tankDir2.put(3, '>');

        for (int tc = 1; tc <= tcCnt; tc++) {

            StringTokenizer st = new StringTokenizer(br.readLine());
            h = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            board = new char[h][w];
            for (int i = 0; i < h; i++) {
                board[i] = br.readLine().toCharArray();
            }
            int n = Integer.parseInt(br.readLine());
            String cmd = br.readLine();

            y = -1;
            x = -1;
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    if (!tankDir.keySet().contains(board[i][j])) continue;
                    y = i;
                    x = j;
                    break;
                }
            }

            for (char c : cmd.toCharArray()) {
                logic(c);
            }

            sb = new StringBuilder();
            sb.append("#").append(tc).append(" ");
            for (int i = 0; i < h; i++) {
                for (int j = 0; j < w; j++) {
                    sb.append(board[i][j]);
                }
                sb.append("\n");
            }
            System.out.print(sb);

        }
    }

    private static void logic(char cmd) {
        if (cmd == 'S') {
            int d = tankDir.get(board[y][x]);
            int by = y;
            int bx = x;
            while (true) {
                by = by + dy[d];
                bx = bx + dx[d];
                if (by >= h || by < 0 || bx >= w || bx < 0 || board[by][bx] == '#')
                    break;
                if (board[by][bx] == '*') {
                    board[by][bx] = '.';
                    break;
                }
            }
            return;
        }

        int d = cmdDir.get(cmd);
        char tank = tankDir2.get(d);
        board[y][x] = tank;
        int ny = y + dy[d];
        int nx = x + dx[d];
        if (ny >= 0 && nx >= 0 && ny < h && nx < w && board[ny][nx] == '.') {
            board[y][x] = '.';
            board[ny][nx] = tank;
            y = ny;
            x = nx;
        }

    }
}