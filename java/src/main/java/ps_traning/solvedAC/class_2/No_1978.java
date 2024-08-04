package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1978 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception {
        int cnt = Integer.parseInt(br.readLine());
        int[] nums = new int[cnt];
        int i = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            nums[i] = Integer.parseInt(st.nextToken());
            i++;
        }
        boolean[] check = new boolean[1001];
        Arrays.fill(check, true);
        check[0] = false;
        check[1] = false;
        for (i = 2; i < 1001; i++) if (check[i]) for (int n = i * 2; n < 1001; n += i) check[n] = false;

        int answer = 0;
        for (int n : nums) if (check[n]) answer++;
        System.out.println(answer);
    }
}
