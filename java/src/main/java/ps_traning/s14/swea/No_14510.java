package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class No_14510 {

    public static void main(String[] args) throws IOException {
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
                maxH = Math.max(maxH, hs[i]);
            }

            int odd = 0;
            int even = 0;
            for (int h : hs) {
                odd += (maxH - h) % 2;
                even += (maxH - h) / 2;
            }

            while (even > odd && Math.abs(even - odd) > 1) {
                even--;
                odd += 2;
            }

            int result = odd * 2;
            if (odd > even) result -= 1;
            if (even > odd) result += 2;
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
