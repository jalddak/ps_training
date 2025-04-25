package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_2819 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());

        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        for (int tc = 1; tc <= tcCnt; tc++) {
            result.append("#").append(tc).append(" ");

            int[][] board = new int[4][4];
            for (int i = 0; i < 4; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 4; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            Set<String> set = new HashSet<>();

            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    Stack<Object[]> stack = new Stack<>();
                    String info = String.valueOf(board[i][j]);
                    stack.push(new Object[]{i, j, info});
                    while (!stack.isEmpty()) {
                        Object[] obj = stack.pop();
                        int y = (int) obj[0];
                        int x = (int) obj[1];
                        info = (String) obj[2];

                        if (info.length() == 7) {
                            set.add(info);
                            continue;
                        }

                        for (int d = 0; d < 4; d++) {
                            int ny = y + dy[d];
                            int nx = x + dx[d];
                            if (ny < 0 || ny >= 4 || nx < 0 || nx >= 4) continue;
                            String nInfo = info + String.valueOf(board[ny][nx]);
                            stack.push(new Object[]{ny, nx, nInfo});
                        }
                    }
                }
            }

            result.append(set.size()).append("\n");
        }
        System.out.print(result);
    }
}
