package ps_traning.s14.test;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Test1 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.parseInt(br.readLine());
            int[] hs = new int[n];
            StringTokenizer st = new StringTokenizer(br.readLine());
            int maxH = 0;
            for (int i = 0; i < n; i++) {
                hs[i] = Integer.parseInt(st.nextToken());
                maxH = Math.max(hs[i], maxH);
            }

            int answer = 0;
            int odd = 0;
            int even = 0;
            for (int i = 0; i < n; i++) {
                odd += (maxH - hs[i]) % 2;
                even += (maxH - hs[i]) / 2;
            }

            while (even > 0 && even - odd > 1) {
                even -= 1;
                odd += 2;
            }

            while (odd > 0 || even > 0) {
                answer += 2;
                odd -= 1;
                even -= 1;
            }

            if (even < 0) answer -= 1;


            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.print(sb);
    }
}

