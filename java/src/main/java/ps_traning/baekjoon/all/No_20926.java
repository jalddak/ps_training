package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_20926 {

    public static int r, c;
    public static char[][] board;
    public static int[] dy = {-1, 0, 1, 0};
    public static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        c = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        int sy = 0;
        int sx = 0;

        board = new char[r][c];
        int[][] visited = new int[r][c];
        for (int i = 0; i < r; i++) {
            board[i] = br.readLine().toCharArray();
            Arrays.fill(visited[i], Integer.MAX_VALUE);
            for (int j = 0; j < c; j++) {
                if (board[i][j] == 'T') {
                    sy = i;
                    sx = j;
                    visited[i][j] = 0;
                    board[i][j] = '0';
                }
            }
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            return a[0] - b[0];
        });

        pq.offer(new int[]{0, sy, sx});
        Set<Character> set = new HashSet<>(List.of('H', 'R', 'E'));

        int answer = -1;
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int cost = poll[0];
            int y = poll[1];
            int x = poll[2];

            if (board[y][x] == 'E') {
                answer = cost;
                break;
            }
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                int temp = 0;
                while (ny >= 0 && nx >= 0 && ny < r && nx < c && !set.contains(board[ny][nx])) {
                    temp += board[ny][nx] - '0';
                    ny += dy[d];
                    nx += dx[d];
                }
                if (ny < 0 || nx < 0 || ny >= r || nx >= c) continue;
                if (board[ny][nx] != 'H' && set.contains(board[ny][nx])) {
                    if (board[ny][nx] == 'R') {
                        ny += dy[d - 2 >= 0 ? d - 2 : d + 2];
                        nx += dx[d - 2 >= 0 ? d - 2 : d + 2];
                        if (visited[ny][nx] <= cost + temp) continue;
                    }
                    visited[ny][nx] = cost + temp;
                    pq.offer(new int[]{cost + temp, ny, nx});
                }

            }
        }

        System.out.println(answer);
    }
}