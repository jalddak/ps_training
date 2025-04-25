package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_7576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.valueOf(st.nextToken());
        int n = Integer.valueOf(st.nextToken());

        Queue<int[]> q = new LinkedList<>();

        int[][] box = new int[n][m];
        for (int y = 0; y < n; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < m; x++) {
                box[y][x] = Integer.valueOf(st.nextToken());
                if (box[y][x] == 1) q.add(new int[]{y, x, 0});
            }
        }


        int answer = 0;
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        while (!q.isEmpty()) {
            int[] r = q.poll();
            int y = r[0], x = r[1], day = r[2];
            answer = day;

            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= 0 && ny < n && nx >= 0 && nx < m && box[ny][nx] == 0) {
                    box[ny][nx] = 1;
                    q.add(new int[]{ny, nx, day + 1});
                }
            }
        }

        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                if (box[y][x] == 0) {
                    answer = -1;
                    break;
                }
            }
        }

        System.out.println(answer);
    }
}
