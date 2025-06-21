package ps_traning.barkingdog.x0B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_11729 {
    private static final StringBuilder sb = new StringBuilder();
    private static int cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        rc(1, 3, n);
        System.out.println(cnt);
        System.out.print(sb);
    }

    private static void rc(int a, int b, int n) {
        if (n == 0) return;
        cnt += 1;
        rc(a, 6 - a - b, n - 1);
        sb.append(a).append(" ").append(b).append("\n");
        rc(6 - a - b, b, n - 1);
    }
}
