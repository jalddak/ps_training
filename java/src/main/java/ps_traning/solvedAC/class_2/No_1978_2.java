package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1978_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = Integer.parseInt(br.readLine());
        int[] nums = new int[cnt];
        int index = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) nums[index++] = Integer.valueOf(st.nextToken());

        boolean[] check = new boolean[1001];
        Arrays.fill(check, true);
        check[0] = false;
        check[1] = false;

        for (int i = 2; i < 1001; i++) {
            if (check[i]) {
                for (int j = 2 * i; j < 1001; j += i) {
                    check[j] = false;
                }
            }
        }

        int answer = 0;
        for (int n : nums) {
            if (check[n]) answer++;
        }

        System.out.println(answer);
    }
}
