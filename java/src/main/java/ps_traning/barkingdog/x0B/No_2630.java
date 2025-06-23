package ps_traning.barkingdog.x0B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class No_2630 {
    private static int n;
    private static int[][] board;
    private static int[] answer = new int[2];
    private static int[] dy = {0, 0, 1, 1};
    private static int[] dx = {0, 1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
            }
        }

        int result = rc(n, 0, 0);
        if (result != 2) answer[result] += 1;
        for (int a : answer) System.out.println(a);
    }

    private static int rc(int l, int y, int x) {
        if (l == 1) return board[y][x];

        List<Integer> check = new ArrayList<>();
        int nl = l / 2;
        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d] * nl;
            int nx = x + dx[d] * nl;
            check.add(rc(nl, ny, nx));
        }

        if (check.stream().collect(Collectors.toSet()).size() == 1 && check.get(0) != 2)
            return check.get(0);

        for (int num : check) {
            if (num == 2) continue;
            answer[num] += 1;
        }

        return 2;
    }
}
