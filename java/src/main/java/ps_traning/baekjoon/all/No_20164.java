package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_20164 {

    private static int minR, maxR;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        minR = -1;
        maxR = -1;

        String num = br.readLine();
        recursion(num, countOdd(num));
        StringBuilder sb = new StringBuilder();
        sb.append(minR).append(" ").append(maxR);
        System.out.println(sb);

    }

    private static int countOdd(String num) {
        int result = 0;
        for (char n : num.toCharArray()) {
            if ((n - '0') % 2 == 1) result++;
        }
        return result;
    }

    private static void recursion(String num, int cnt) {

        int len = num.length();

        if (len == 1) {
            minR = minR == -1 ? cnt : Math.min(minR, cnt);
            maxR = maxR == -1 ? cnt : Math.max(maxR, cnt);
            return;
        }

        if (len == 2) {
            String next = String.valueOf((num.charAt(0) - '0') + (num.charAt(1) - '0'));
            recursion(next, cnt + countOdd(next));
            return;
        }

        for (int i = 1; i < len - 1; i++) {
            int first = Integer.parseInt(num.substring(0, i));
            for (int j = i + 1; j < len; j++) {
                int second = Integer.parseInt(num.substring(i, j));
                int third = Integer.parseInt(num.substring(j));
                String next = String.valueOf(first + second + third);
                recursion(next, cnt + countOdd(next));
            }
        }
    }
}
