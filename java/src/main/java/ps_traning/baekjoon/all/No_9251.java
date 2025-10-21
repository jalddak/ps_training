package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_9251 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();

        int[][] cnt = new int[a.length() + 1][b.length() + 1];

        for (int i = 0; i < a.length(); i++) {
            for (int j = 0; j < b.length(); j++) {
                cnt[i + 1][j + 1] = Math.max(
                        cnt[i][j] + (a.charAt(i) == b.charAt(j) ? 1 : 0),
                        Math.max(cnt[i + 1][j], cnt[i][j + 1]));
            }
        }

        System.out.println(cnt[a.length()][b.length()]);
    }
}
