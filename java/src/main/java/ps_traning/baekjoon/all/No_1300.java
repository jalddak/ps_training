package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;

class No_1300 {

    private static int n, k;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        k = Math.min(k, 1000000000);
        long answer = binarySearch();
        System.out.println(answer);

    }

    private static long binarySearch() {

        long l = 1L;
        long r = (long) n * n + 1;

        long result = 1;
        while (l + 1 < r) {
            long mid = (l + r) / 2;
            long[] temp = check(mid);
            if (temp[0] <= k && temp[1] >= k) {
                result = temp[2];
                break;
            } else if (temp[0] < k) l = mid;
            else r = mid;
        }

        return result;

    }

    private static long[] check(long num) {
        long maxNum = 0;
        long maxCnt = 0;
        long minCnt = maxCnt;

        for (int i = 1; i <= n; i++) {
            long temp = Math.min(num / i, n);
            if (temp == 0) break;
            maxCnt += temp;
            if (maxNum < temp * i) {
                maxNum = temp * i;
                minCnt = 0;
            } else if (maxNum == temp * i) minCnt -= 1;
        }
        minCnt += maxCnt;

        return new long[]{minCnt, maxCnt, maxNum};
    }
}

