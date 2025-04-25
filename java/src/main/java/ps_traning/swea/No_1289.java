package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_1289 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            String input = br.readLine();

            char cur = '0';
            int result = 0;
            for (char bit : input.toCharArray()) {
                if (bit != cur) {
                    cur = bit;
                    result++;
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
