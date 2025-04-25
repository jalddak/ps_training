package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class No_11286 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.valueOf(br.readLine());
        PriorityQueue<int[]> pq = new PriorityQueue(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1];
            }
        });
        for (int i = 0; i < n; i++) {
            int num = Integer.valueOf(br.readLine());
            if (num == 0) {
                int result = 0;
                if (!pq.isEmpty()) {
                    result = pq.poll()[1];
                }
                sb.append(result).append("\n");
            } else {
                pq.add(new int[]{Math.abs(num), num});
            }
        }

        System.out.print(sb.toString());
    }
}
