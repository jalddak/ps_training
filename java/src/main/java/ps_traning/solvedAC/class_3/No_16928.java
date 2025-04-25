package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_16928 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());

        Map<Integer, Integer> ls = new HashMap<>();
        for (int i = 0; i < n + m; i++) {
            st = new StringTokenizer(br.readLine());
            ls.put(Integer.valueOf(st.nextToken()), Integer.valueOf(st.nextToken()));
        }

        int[] board = new int[101];
        Arrays.fill(board, -1);

        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        board[1] = 0;

        while (!q.isEmpty()) {
            int x = q.poll();
            for (int i = 1; i < 7; i++) {
                int nx = x + i;
                if (ls.containsKey(nx)) nx = ls.get(nx);
                if (board[nx] == -1 || board[nx] > board[x] + 1) {
                    board[nx] = board[x] + 1;
                    q.add(nx);
                }
                if (nx == 100) {
                    System.out.println(board[nx]);
                    System.exit(0);
                }
            }

        }
    }
}
