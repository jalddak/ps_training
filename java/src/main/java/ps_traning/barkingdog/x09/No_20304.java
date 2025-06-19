package ps_traning.barkingdog.x09;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_20304 {
    private static final Queue<Integer> queue = new LinkedList<>();
    private static int n, cnt, length, answer;
    private static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.valueOf(br.readLine());
        cnt = Integer.valueOf(br.readLine());


        length = Integer.toBinaryString(n).length();
        arr = new int[n + 1];
        Arrays.fill(arr, 100);

        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int num = Integer.valueOf(st.nextToken());
            queue.offer(num);
            arr[num] = 0;
        }

        answer = 0;
        while (!queue.isEmpty()) {
            int num = queue.poll();
            xor(num);
        }
        System.out.println(answer);

    }

    private static void xor(int num) {
        for (int i = 0; i < length; i++) {
            int temp = num ^ (1 << i);
            if (temp > n) continue;
            if (arr[temp] <= arr[num] + 1) continue;
            arr[temp] = arr[num] + 1;
            answer = arr[temp];
            queue.offer(temp);
        }
    }
}
