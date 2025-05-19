package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1860 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int[] secs = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                secs[i] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(secs);
            int max_s = secs[n - 1];
            String result = "Possible";
            int si = 0;
            int cur = 0;
            for (int i = 0; i <= max_s; i++) {
                if (i != 0 && i % m == 0) {
                    cur += k;
                }
                if (secs[si] <= i) {
                    si++;
                    cur--;
                }
                if (cur < 0) {
                    result = "Impossible";
                    break;
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
