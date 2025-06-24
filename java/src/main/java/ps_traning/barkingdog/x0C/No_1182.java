package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1182 {
    private static int n, s, answer;
    private static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        s = Integer.valueOf(st.nextToken());
        nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) nums[i] = Integer.valueOf(st.nextToken());
        back(0, 0);
        System.out.println(answer);
    }

    private static void back(int start, int result) {
        for (int i = start; i < n; i++) {
            result += nums[i];
            if (result == s) answer++;
            back(i + 1, result);
            result -= nums[i];
        }
    }
}
