package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_9663 {

    private static int[] arr;
    private static int answer = 0;
    private static int n;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        arr = new int[n];
        logic(0);
        System.out.println(answer);
    }

    private static void logic(int depth) {
        if (depth == n) {
            answer++;
            return;
        }

        for (int i = 0; i < n; i++) {
            boolean flag = true;
            for (int j = 0; j < depth; j++) {
                if (i != arr[j] && depth - j != Math.abs(i - arr[j])) continue;
                flag = false;
                break;
            }
            if (flag) {
                arr[depth] = i;
                logic(depth + 1);
            }
        }
    }
}
