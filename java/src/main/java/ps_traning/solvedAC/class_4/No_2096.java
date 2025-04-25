package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_2096 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n1 = Integer.valueOf(st.nextToken());
        int n2 = Integer.valueOf(st.nextToken());
        int n3 = Integer.valueOf(st.nextToken());
        int[][] dp = {{n1, n2, n3}, {n1, n2, n3}};

        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            n1 = Integer.valueOf(st.nextToken());
            n2 = Integer.valueOf(st.nextToken());
            n3 = Integer.valueOf(st.nextToken());
            int[][] temp = {
                    {
                            Arrays.stream(Arrays.copyOfRange(dp[0], 0, 2)).max().getAsInt() + n1,
                            Arrays.stream(dp[0]).max().getAsInt() + n2,
                            Arrays.stream(Arrays.copyOfRange(dp[0], 1, 3)).max().getAsInt() + n3
                    },
                    {
                            Arrays.stream(Arrays.copyOfRange(dp[1], 0, 2)).min().getAsInt() + n1,
                            Arrays.stream(dp[1]).min().getAsInt() + n2,
                            Arrays.stream(Arrays.copyOfRange(dp[1], 1, 3)).min().getAsInt() + n3
                    }
            };

            dp = temp;
        }

        System.out.println(Arrays.stream(dp[0]).max().getAsInt() + " " + Arrays.stream(dp[1]).min().getAsInt());
    }
}
