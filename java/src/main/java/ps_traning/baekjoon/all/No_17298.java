package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_17298 {

    public static int n;
    public static int[] arr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] answer = new int[n];
        Arrays.fill(answer, -1);

        Stack<int[]> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && stack.peek()[1] < arr[i]) {
                int[] pop = stack.pop();
                answer[pop[0]] = arr[i];
            }

            stack.push(new int[]{i, arr[i]});
        }

        StringBuffer sb = new StringBuffer();
        for (int a : answer) sb.append(a).append(" ");

        System.out.println(sb);
    }

}