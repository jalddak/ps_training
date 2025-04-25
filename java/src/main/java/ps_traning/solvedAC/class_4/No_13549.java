package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_13549 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.valueOf(st.nextToken());
        int e = Integer.valueOf(st.nextToken());

        int[] check = new int[100001];
        Arrays.fill(check, 100001);
        check[s] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        pq.add(new int[]{0, s});

        while (!pq.isEmpty()) {
            int[] pqr = pq.poll();
            int t = pqr[0], x = pqr[1];
            if (x == e) {
                System.out.println(t);
                break;
            }

            int[] nums = {2 * x, x - 1, x + 1};
            for (int i = 0; i < 3; i++) {
                int nt = i == 0 ? t : t + 1;
                int num = nums[i];
                if (num > 100000 || num < 0 || check[num] <= nt) continue;
                pq.add(new int[]{nt, num});
                check[num] = nt;
            }
        }
    }
}
