package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class No_1873 {

    private static final int[] dy = {-1, 0, 1, 0};
    private static final int[] dx = {0, 1, 0, -1};

    private static final Map<Character, Integer> cmdToIndex = new HashMap<>();
    private static final Map<Character, Character> cmdToChar = new HashMap<>();
    private static final Map<Character, Integer> charToIndex = new HashMap<>();

    public static void main(String[] args) throws IOException {

        char[] charArr = {'^', '>', 'v', '<'};
        char[] cmdArr = {'U', 'R', 'D', 'L'};
        for (int i = 0; i < 4; i++) {
            cmdToIndex.put(cmdArr[i], i);
            cmdToChar.put(cmdArr[i], charArr[i]);
            charToIndex.put(charArr[i], i);
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());

        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int h = Integer.valueOf(st.nextToken());
            int w = Integer.valueOf(st.nextToken());

            char[][] board = new char[h][w];
            for (int i = 0; i < h; i++) {
                String row = br.readLine();
                for (int j = 0; j < w; j++) {
                    board[i][j] = row.charAt(j);
                }
            }

            int n = Integer.valueOf(br.readLine());
            String cmds = br.readLine();

            board = solution(h, w, board, n, cmds);

            for (char[] row : board) {
                sb.append(String.valueOf(row)).append("\n");
            }
        }
        System.out.print(sb);
    }

    private static char[][] solution(int h, int w, char[][] board, int n, String cmds) {
        int y = -1, x = -1;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (charToIndex.containsKey(board[i][j])) {
                    y = i;
                    x = j;
                    break;
                }
            }
        }

        for (char cmd : cmds.toCharArray()) {
            if (cmd != 'S') {
                int ny = y + dy[cmdToIndex.get(cmd)];
                int nx = x + dx[cmdToIndex.get(cmd)];
                board[y][x] = cmdToChar.get(cmd);

                if (ny < 0 || ny >= h || nx < 0 || nx >= w) continue;
                if (board[ny][nx] == '.') {
                    board[ny][nx] = board[y][x];
                    board[y][x] = '.';
                    y = ny;
                    x = nx;
                }
            } else {
                int sy = y;
                int sx = x;
                while (true) {
                    sy += dy[charToIndex.get(board[y][x])];
                    sx += dx[charToIndex.get(board[y][x])];
                    if (sy < 0 || sy >= h || sx < 0 || sx >= w || board[sy][sx] == '#') break;
                    if (board[sy][sx] == '*') {
                        board[sy][sx] = '.';
                        break;
                    }
                }

            }
        }
        return board;
    }
}
