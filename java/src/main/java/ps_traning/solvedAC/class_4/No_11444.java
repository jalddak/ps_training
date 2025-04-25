package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class No_11444 {
    /*
    도가뉴 항등식 알아야함. 모르면 초월적으로 풀어야함. 개 억까문제.
     */

    private static Map<Long, Long> checked;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.valueOf(br.readLine());
        checked = new HashMap<>();
        System.out.println(fibo(n));

    }

    private static long fibo(long n) {
        if (!checked.containsKey(n)) {

            if (n == 0) checked.put(n, 0L);
            else if (n == 1) checked.put(n, 1L);
            else if (n % 2 == 0) {
                long fn = fibo(n / 2);
                long fnMinus1 = fibo(n / 2 - 1);
                checked.put(n, (fn * (fn + 2 * fnMinus1)) % 1000000007);
            } else {
                long fn = fibo(n / 2);
                long fnPlus1 = fibo(n / 2 + 1);
                checked.put(n, (fn * fn + fnPlus1 * fnPlus1) % 1000000007);
            }
        }
        return checked.get(n);
    }
}
