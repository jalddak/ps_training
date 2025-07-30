package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_2477 {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.valueOf(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int d = Integer.valueOf(st.nextToken());
        int len = Integer.valueOf(st.nextToken());
        int before = len;
        int first = len;

        int[] temp = new int[6];
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            d = Integer.valueOf(st.nextToken());
            len = Integer.valueOf(st.nextToken());
            temp[i] = before * len;
            before = len;
        }

        temp[5] = first * before;
        System.out.println(k * (Arrays.stream(temp).sum() - 2 * Arrays.stream(temp).max().getAsInt()));
    }

}