package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_1225 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int tcCnt = 1; tcCnt <= 10; tcCnt++) {
            int tc = Integer.valueOf(br.readLine());
            sb.append("#").append(tc).append(" ");

            Queue<Integer> q = new LinkedList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 8; i++) {
                q.offer(Integer.valueOf(st.nextToken()));
            }

            int x = 1;
            while (true) {
                int n = q.poll();
                n = n - x > 0 ? n - x : 0;
                x = x + 1 <= 5 ? x + 1 : 1;
                q.offer(n);
                if (n == 0) break;
            }

            while (!q.isEmpty()) {
                sb.append(q.poll()).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}
