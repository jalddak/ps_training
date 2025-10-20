package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_2447 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        String[] result = recursion(n);
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append("\n");
        }
        System.out.print(sb);
    }

    private static String[] recursion(int len) {
        if (len == 1) {
            return new String[]{"*"};
        }

        String[] result = new String[len];
        String[] before = recursion(len / 3);
        StringBuilder normal = new StringBuilder();
        StringBuilder middle = new StringBuilder();
        StringBuilder blank = new StringBuilder();
        for (int i = 0; i < len / 3; i++) blank.append(" ");
        for (int i = 0; i < len / 3; i++) {
            for (int j = 0; j < 3; j++) {
                normal.append(before[i]);
                middle.append(j != 1 ? before[i] : blank.toString());
            }
            result[i] = normal.toString();
            result[i + len / 3] = middle.toString();
            result[i + (len / 3 * 2)] = normal.toString();
            normal.setLength(0);
            middle.setLength(0);
        }
        return result;

    }
}
