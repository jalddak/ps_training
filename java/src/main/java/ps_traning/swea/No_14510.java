package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_14510 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());
            int[] arr = new int[n];
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int i = 0; i < n; i++) {
                arr[i] = Integer.valueOf(st.nextToken());
            }
            int maxH = Arrays.stream(arr).max().getAsInt();

            int odd = 0;
            int even = 0;
            for (int h : arr){
                int t = maxH - h;
                odd += t % 2;
                even += t / 2;
            }
            int result = 0;

            if (even > odd) {
                while (Math.abs(even - odd) > 1) {
                    even--;
                    odd += 2;
                }
            }

            if (odd > even) result = 2 * odd - 1;
            else if (odd == even) result = odd * 2;
            else result = even * 2;

            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);

    }
}
