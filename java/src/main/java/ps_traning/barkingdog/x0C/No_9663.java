package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_9663 {
    private static int n, answer;
    private static int[] loca;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        answer = 0;
        loca = new int[n];
        Arrays.fill(loca, -1);
        back(0);
        System.out.println(answer);

    }

    private static void back(int depth) {
        if (depth == n) {
            answer++;
            return;
        }

        for (int i = 0; i < n; i++) {
            boolean flag = true;
            for (int j = 0; j < depth; j++) {
                if (loca[j] == i || Math.abs(loca[j] - i) == Math.abs(j - depth)) {
                    flag = false;
                    break;
                }
            }
            if (!flag) continue;
            loca[depth] = i;
            back(depth + 1);
        }
    }
}
