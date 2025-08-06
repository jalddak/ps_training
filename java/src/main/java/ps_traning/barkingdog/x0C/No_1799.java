package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_1799 {

    private static int n;
    private static int[][] board;
    private static List<int[]> odd, even;
    private static boolean[] diag1, diag2;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        diag1 = new boolean[2 * n - 1];
        diag2 = new boolean[2 * n - 1];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        odd = new ArrayList<>();
        even = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0) continue;
                if ((i + j) % 2 == 0) even.add(new int[]{i, j});
                else odd.add(new int[]{i, j});
            }
        }

        System.out.println(recursion(0, 0, odd, 0) + recursion(0, 0, even, 0));
    }

    private static int recursion(int idx, int cnt, List<int[]> list, int result) {
        if (cnt + list.size() - idx <= result) return result;

        boolean flag = true;
        for (int i = idx; i < list.size(); i++) {
            int y = list.get(i)[0], x = list.get(i)[1];
            if (!check(y, x)) continue;
            flag = false;
            diag1[y + x] = true;
            diag2[y - x + (n - 1)] = true;
            cnt += 1;
            result = Math.max(result, recursion(i + 1, cnt, list, result));
            diag2[y - x + (n - 1)] = false;
            diag1[y + x] = false;
            cnt -= 1;
        }

        if (flag) {
            result = Math.max(result, cnt);
        }

        return result;
    }

    private static boolean check(int y, int x) {
        return !diag1[y + x] && !diag2[y - x + (n - 1)];
    }
}
