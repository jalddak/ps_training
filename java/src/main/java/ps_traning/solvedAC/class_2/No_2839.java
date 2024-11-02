package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_2839 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int a = n / 5;
        int x = n % 5;
        while (a > -1 && x % 3 != 0) {
            a -= 1;
            x += 5;
        }
        if (a == -1) System.out.println(-1);
        else System.out.println(a + x / 3);
    }
}
