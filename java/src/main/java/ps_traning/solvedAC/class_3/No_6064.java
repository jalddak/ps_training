package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_6064 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.valueOf(st.nextToken());
            int n = Integer.valueOf(st.nextToken());
            int x = Integer.valueOf(st.nextToken());
            int y = Integer.valueOf(st.nextToken());

            int answer = x;
            int a = x;
            int b = x % n;
            if (b == 0) b = n;

            int end = lcm(m, n);
            boolean flag = false;

            while (answer <= end) {
                if (a == x && b == y) {
                    flag = true;
                    break;
                }
                answer += m;
                b += m;
                b %= n;
                if (b == 0) b = n;
            }
            if (!flag) answer = -1;
            sb.append(answer).append("\n");
        }

        System.out.print(sb.toString());
    }

    public static int gcd(int m, int n) {
        while (n != 0) {
            int temp = m % n;
            m = n;
            n = temp;
        }
        return m;
    }

    public static int lcm(int m, int n) {
        return m * n / gcd(m, n);
    }
}
