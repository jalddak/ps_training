package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_7569 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.valueOf(st.nextToken());
        int n = Integer.valueOf(st.nextToken());
        int h = Integer.valueOf(st.nextToken());

        Queue<int[]> q = new LinkedList<>();

        int[][][] box = new int[h][n][m];
        for (int z = 0; z < h; z++) {
            for (int y = 0; y < n; y++) {
                st = new StringTokenizer(br.readLine());
                for (int x = 0; x < m; x++) {
                    box[z][y][x] = Integer.valueOf(st.nextToken());
                    if (box[z][y][x] == 1) q.add(new int[]{z, y, x, 0});
                }
            }
        }


        int answer = 0;
        int[] dz = {0, 0, 0, 0, 1, -1};
        int[] dy = {-1, 0, 1, 0, 0, 0};
        int[] dx = {0, 1, 0, -1, 0, 0};

        while (!q.isEmpty()) {
            int[] r = q.poll();
            int z = r[0], y = r[1], x = r[2], day = r[3];
            answer = day;

            for (int d = 0; d < 6; d++) {
                int nz = z + dz[d];
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (nz >= 0 && nz < h && ny >= 0 && ny < n && nx >= 0 && nx < m && box[nz][ny][nx] == 0) {
                    box[nz][ny][nx] = 1;
                    q.add(new int[]{nz, ny, nx, day + 1});
                }
            }
        }

        for (int z = 0; z < h; z++) {
            for (int y = 0; y < n; y++) {
                for (int x = 0; x < m; x++) {
                    if (box[z][y][x] == 0) {
                        answer = -1;
                        break;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
