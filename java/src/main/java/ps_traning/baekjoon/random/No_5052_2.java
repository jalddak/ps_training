package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_5052_2 {

    private static int n;
    private static String[] numbers;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            n = Integer.valueOf(br.readLine());
            numbers = new String[n];
            for (int j = 0; j < n; j++) {
                numbers[j] = br.readLine();
            }
            Arrays.sort(numbers);

            String result = "YES";
            for (int j = 0; j < n - 1; j++) {
                if (numbers[j].length() >= numbers[j + 1].length()) continue;
                boolean flag = true;
                for (int k = 0; k < numbers[j].length(); k++) {
                    if (numbers[j].charAt(k) != numbers[j + 1].charAt(k)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    result = "NO";
                    break;
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
