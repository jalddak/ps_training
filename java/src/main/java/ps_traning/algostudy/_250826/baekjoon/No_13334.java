package ps_traning.algostudy._250826.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_13334 {

    private static int n, d;
    private static int[][] infos;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        infos = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] info = new int[2];
            info[0] = Integer.parseInt(st.nextToken());
            info[1] = Integer.parseInt(st.nextToken());
            Arrays.sort(info);
            infos[i] = info;
        }
        Arrays.sort(infos, (a, b) -> {
            if (a[1] == b[1]) return a[0] - b[0];
            return a[1] - b[1];
        });

        d = Integer.parseInt(br.readLine());

        int result = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return a[0] - b[0];
        });
        for (int i = 0; i < n; i++) {
            int s = infos[i][0];
            int e = infos[i][1];
            if (e - s > d) continue;
            while (!pq.isEmpty() && pq.peek()[1] < e) {
                pq.poll();
            }
            pq.offer(new int[]{s, s + d});
            result = Math.max(result, pq.size());
        }

        System.out.println(result);
    }
}
