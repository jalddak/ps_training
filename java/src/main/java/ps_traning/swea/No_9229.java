package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_9229 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int m = Integer.valueOf(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int[] ws = new int[n];
            for (int i = 0; i < n; i++) {
                ws[i] = Integer.valueOf(st.nextToken());
            }
            Arrays.sort(ws);
            int l = 0;
            int r = n-1;

            int result = -1;
            while (l < r) {
                int temp = ws[l] + ws[r];
                if (temp == m) {
                    result = temp;
                    break;
                } else if (temp > m){
                    r -= 1;
                } else {
                    l += 1;
                    result = Math.max(result, temp);
                }
            }
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
