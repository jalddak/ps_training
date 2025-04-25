package ps_traning.solvedAC.class_4;

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

        System.out.println(dv(a, b, c));
    }

    private static long dv(long a, long b, long c) {
        if (b == 1) return a % c;
        else if (b == 2) return (a % c) * (a % c) % c;
        else {
            long temp = dv(a, b / 2, c);
            if (b % 2 == 0) return temp * temp % c;
            else return ((temp % c) * (temp % c) % c) * (a % c) % c;
        }
    }
}
