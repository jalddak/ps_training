package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

import static java.lang.System.exit;

public class No_1414 {

    private static int n, result;
    private static char[][] board;
    private static Map<Character, Integer> fm = new HashMap<>();
    private static PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    private static boolean[] visited;

    public static void main(String[] args) throws Exception {

        for (char t = 'A'; t - 1 != 'Z'; t++) {
            fm.put(t, t - 'A' + 27);
            char temp = Character.toLowerCase(t);
            fm.put(temp, temp - 'a' + 1);
        }
        fm.put('0', 53);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        board = new char[n][n];
        visited = new boolean[n];
        result = 0;

        char len = ' ';
        int start = -1;

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = input.charAt(j);
                if (board[i][j] == '0') continue;
                result += fm.get(board[i][j]);
                if (i == j) continue;
                if (start == -1 || fm.get(len) > fm.get(board[i][j])) {
                    start = i;
                    len = board[i][j];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (board[i][j] != board[j][i]) {
                    char temp = fm.get(board[i][j]) > fm.get(board[j][i]) ? board[j][i] : board[i][j];
                    board[i][j] = temp;
                    board[j][i] = temp;
                }
            }
        }

        if (start == -1) {
            if (n == 1) System.out.println(board[0][0] == '0' ? 0 : fm.get(board[0][0]));
            else System.out.println(-1);
            exit(0);
        }

        pq.offer(new int[]{0, start});

        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int l = poll[0], node = poll[1];
            if (visited[node]) continue;
            visited[node] = true;
            result -= l;
            for (int i = 0; i < n; i++) {
                if (node == i || board[node][i] == '0') continue;
                pq.offer(new int[]{fm.get(board[node][i]), i});
            }
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                result = -1;
                break;
            }
        }

        System.out.println(result);
    }
}
