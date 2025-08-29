package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class No_2382_long {

    private static int answer, n, m, k;
    private static int[] dy = {0, -1, 1, 0, 0};
    private static int[] dx = {0, 0, 0, -1, 1};
    private static Map<Long, int[]> infos;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            answer = 0;
            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
                return a[2] - b[2];
            });
            for (int i = 0; i < k; i++) {
                int[] info = new int[4];
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 4; j++) {
                    info[j] = Integer.parseInt(st.nextToken());
                }
                pq.offer(info);
            }

            for (int i = 0; i < m; i++) {
                move(pq);
                remove();
                for (long key : infos.keySet()) {
                    int y = (int) (key >> 32), x = (int) key;
                    int[] info = infos.get(key);
                    pq.offer(new int[]{y, x, info[0], info[1]});
                }
            }

            while (!pq.isEmpty()) {
                answer += pq.poll()[2];
            }
            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.println(sb);
    }

    private static void move(PriorityQueue<int[]> pq) {
        infos = new HashMap<>();
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int y = poll[0], x = poll[1], cnt = poll[2], d = poll[3];
            int ny = y + dy[d], nx = x + dx[d];
            long key = ((long) ny << 32) + nx;
            if (!infos.containsKey(key)) infos.put(key, new int[]{0, 0});
            int[] info = infos.get(key);
            info[0] += cnt;
            info[1] = d;
        }
    }

    private static void remove() {
        for (long key : infos.keySet()) {
            int y = (int) (key >> 32), x = (int) key;
            int[] info = infos.get(key);
            if (y == 0 || x == 0 || y == n - 1 || x == n - 1) {
                info[0] /= 2;
                info[1] = info[1] % 2 == 1 ? info[1] + 1 : info[1] - 1;
            }
        }
    }
}

