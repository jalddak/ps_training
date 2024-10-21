package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_2775 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        for (int i = 0; i < t; i++) {
            int k = Integer.valueOf(br.readLine());
            int n = Integer.valueOf(br.readLine());
            int[][] apt = new int[k + 1][n + 1];
            for (int j = 1; j <= n; j++) apt[0][j] = j;
            for (int f = 1; f <= k; f++) {
                int s = 0;
                for (int r = 1; r <= n; r++) {
                    s += apt[f - 1][r];
                    apt[f][r] = s;
                }
            }
            System.out.println(apt[k][n]);
        }
    }
}
