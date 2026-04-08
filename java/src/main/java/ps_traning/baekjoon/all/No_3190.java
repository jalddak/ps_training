package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_3190 {

    private static int n, k, l;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};
    private static Queue<Node> nodes = new ArrayDeque<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        int[][] board = new int[n][n];
        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken()) - 1;
            int x = Integer.parseInt(st.nextToken()) - 1;
            board[y][x] = 9;
        }

        l = Integer.parseInt(br.readLine());
        for (int i = 0; i < l; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            char d = st.nextToken().charAt(0);
            nodes.add(new Node(m, d));
        }

        int answer = 0;
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, 1});
        board[0][0] = 1;
        Queue<int[]> bam = new ArrayDeque<>();
        bam.offer(new int[]{0, 0});

        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int hy = poll[0], hx = poll[1], d = poll[2];
            answer += 1;

            int nhy = hy + dy[d];
            int nhx = hx + dx[d];

            if (nhy >= n || nhy < 0 || nhx >= n || nhx < 0 || board[nhy][nhx] == 1)
                break;

            if (board[nhy][nhx] != 9) {
                int[] bamPoll = bam.poll();
                int ty = bamPoll[0], tx = bamPoll[1];
                board[ty][tx] = 0;
            }

            board[nhy][nhx] = 1;
            bam.offer(new int[]{nhy, nhx});

            int nd = d;
            if (!nodes.isEmpty() && nodes.peek().m == answer) {
                Node node = nodes.poll();
                if (node.d == 'L') nd = nd - 1 >= 0 ? nd - 1 : nd + 3;
                else nd = nd + 1 < 4 ? nd + 1 : nd - 3;
            }

            q.offer(new int[]{nhy, nhx, nd});

        }

        System.out.println(answer);
    }

    static class Node {
        int m;
        char d;

        public Node(int m, char d) {
            this.m = m;
            this.d = d;
        }
    }
}