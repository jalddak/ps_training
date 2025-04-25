package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_16953 {
    private static BufferedReader br;
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        long a = Long.valueOf(st.nextToken());
        long b = Long.valueOf(st.nextToken());

        Queue<long[]> q = new LinkedList<>();
        q.add(new long[]{a, 1});

        long answer = -1;
        while (!q.isEmpty()) {
            long[] qr = q.poll();
            long n = qr[0], cnt = qr[1];
            long n1 = n * 2;
            long n2 = n * 10 + 1;

            if (n == b) {
                answer = cnt;
                break;
            }
            if (n1 > b && n2 > b) continue;
            q.add(new long[]{n1, cnt + 1});
            q.add(new long[]{n2, cnt + 1});

        }

        System.out.println(answer);
    }
}
