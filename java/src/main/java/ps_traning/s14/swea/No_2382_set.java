package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.StringTokenizer;

class No_2382_set {

    private static int answer, n, m, k;
    private static int[] dy = {0, -1, 1, 0, 0};
    private static int[] dx = {0, 0, 0, -1, 1};
    private static Set<Integer> set;
    private static int[] cnts = new int[20000];
    private static int[] ds = new int[20000];
    private static PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
        return b[2] - a[2];
    });

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

            for (int i = 0; i < k; i++) {
                int[] info = new int[4];
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 4; j++) {
                    info[j] = Integer.parseInt(st.nextToken());
                }
                pq.offer(info);
            }

            for (int i = 0; i < m; i++) {
                set = new HashSet<>();
                move(pq);
                remove();
                for (int key : set) {
                    int y = (key >> 7), x = key & 0x7f;
                    pq.offer(new int[]{y, x, cnts[key], ds[key]});
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
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int y = poll[0], x = poll[1], cnt = poll[2], d = poll[3];
            int ny = y + dy[d], nx = x + dx[d];
            int key = (ny << 7) + nx;
            if (!set.contains(key)) {
                set.add(key);
                cnts[key] = cnt;
                ds[key] = d;
                continue;
            }
            cnts[key] += cnt;
        }
    }

    private static void remove() {
        for (int key : set) {
            int y = (key >> 7), x = key & 0x7f;
            if (y == 0 || x == 0 || y == n - 1 || x == n - 1) {
                cnts[key] /= 2;
                ds[key] = ds[key] % 2 == 1 ? ds[key] + 1 : ds[key] - 1;
            }
        }
    }
}

