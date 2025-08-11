package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_2492 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] cs = new int[t][2];
        Set<Integer> xs = new HashSet<>();
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            cs[i][0] = x;
            cs[i][1] = Integer.parseInt(st.nextToken());
            xs.add(x);
        }

        Arrays.sort(cs, (a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });

        List<Integer> xsList = new ArrayList<>(xs);
        xsList.sort(Comparator.naturalOrder());

        int cnt = 0;
        int x = 0;
        int y = 0;

        for (int num : xsList) {
            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
                if (a[1] != b[1]) return a[1] - b[1];
                return a[0] - b[0];
            });
            for (int[] c : cs) {
                if (c[0] >= num && c[0] <= num + k) pq.offer(c);
                else if (c[0] > num + k) break;
            }

            Queue<int[]> q = new ArrayDeque<>();
            while (!pq.isEmpty()) {
                if (!q.isEmpty() && q.peek()[1] + k < pq.peek()[1]) {
                    if (cnt < q.size()) {
                        cnt = q.size();
                        x = num;
                        y = q.peek()[1] + k;
                        if (x + k > n) x -= (x + k - n);
                        if (y > m) y = m;
                    }
                    while (!q.isEmpty() && q.peek()[1] + k < pq.peek()[1]) q.poll();
                }
                q.offer(pq.poll());
            }
            if (cnt < q.size()) {
                cnt = q.size();
                x = num;
                y = q.peek()[1] + k;
                if (x + k > n) x -= (x + k - n);
                if (y > m) y = m;
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(x).append(" ").append(y).append("\n").append(cnt);
        System.out.println(sb);
    }

}
