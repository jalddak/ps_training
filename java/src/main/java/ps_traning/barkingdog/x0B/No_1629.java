package ps_traning.barkingdog.x0B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1629 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long a = Long.valueOf(st.nextToken());
        long b = Long.valueOf(st.nextToken());
        long c = Long.valueOf(st.nextToken());

        System.out.println(recursion(a, b, c));
    }

    private static long recursion(long a, long b, long c) {
        if (b == 1) return a % c;
        long temp = recursion(a, b / 2, c);
        if (b % 2 == 1) return ((temp * temp) % c) * (a % c) % c;
        else return temp * temp % c;
    }
}
