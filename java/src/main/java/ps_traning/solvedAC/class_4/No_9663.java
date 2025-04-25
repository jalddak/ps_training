package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_9663 {
    private static int n, answer;
    private static int[] check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        check = new int[n];
        answer = 0;
        solution(0);
        System.out.println(answer);
    }

    private static void solution(int depth) {
        if (depth == n) {
            answer++;
            return;
        }

        for (int i = 0; i < n; i++) {
            boolean flag = false;
            for (int j = 0; j < depth; j++) {
                if (check[j] == i || Math.abs(check[j] - i) == Math.abs(depth - j)) {
                    flag = true;
                    break;
                }
            }
            if (flag) continue;
            check[depth] = i;
            solution(depth + 1);
        }
    }
}
