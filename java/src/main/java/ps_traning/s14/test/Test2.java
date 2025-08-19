package ps_traning.s14.test;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Test2 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int answer = 0;
            int cnt = 0;
            int a = n - m;
            boolean[] check = new boolean[n + 1];
            for (int i = n; i > 0; i--) {
                if (a == 0) break;
                if (i % k == 0) {
                    a--;
                    check[i] = true;
                }
            }

            for (int i = 1; i <= n; i++) {
                if (m == 0) break;
                if (check[i]) {
                    cnt = 0;
                    continue;
                }
                m--;
                answer++;
                cnt++;
                if (cnt == k) {
                    answer *= 2;
                    cnt = 0;
                }

            }


            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.print(sb);
    }
}
