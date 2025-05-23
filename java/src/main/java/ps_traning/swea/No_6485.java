package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_6485 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());

        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());

            int[] preSum = new int[5001];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.valueOf(st.nextToken());
                int b = Integer.valueOf(st.nextToken());
                preSum[a] += 1;
                if (b+1 > 5000) continue;
                preSum[b+1] -= 1;
            }

            for (int i = 1; i <= 5000; i++) {
                preSum[i] += preSum[i - 1];
            }

            int p = Integer.valueOf(br.readLine());
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < p; i++) {
                result.append(preSum[Integer.valueOf(br.readLine())]).append(" ");
            }


            sb.append("#").append(tc).append(" ").append(result.toString()).append("\n");
        }
        System.out.println(sb);
    }
}
