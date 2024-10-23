package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_1676 {
    public static void main(String[] args) throws IOException {
        int n = Integer.valueOf(new BufferedReader(new InputStreamReader(System.in)).readLine());
        int[] cnts = new int[2];
        for (int i = 1; i <= n; i++) {
            int cnt = 0;
            int num = i;
            while (num % 2 == 0) {
                num /= 2;
                cnt++;
            }
            cnts[0] += cnt;
            cnt = 0;
            while (num % 5 == 0) {
                num /= 5;
                cnt++;
            }
            cnts[1] += cnt;
        }
        System.out.println(Arrays.stream(cnts).min().getAsInt());
    }
}
