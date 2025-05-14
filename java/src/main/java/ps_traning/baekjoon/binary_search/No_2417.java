package ps_traning.baekjoon.binary_search;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_2417 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.valueOf(br.readLine());
        binarySearch(0, n, n);
    }

    private static void binarySearch(long s, long e, long n) {
        while (s + 1 < e) {
            long mid = (s + e) / 2;
            if (Math.pow(mid, 2) < n) s = mid;
            else e = mid;
        }
        System.out.println(e);
    }

}
