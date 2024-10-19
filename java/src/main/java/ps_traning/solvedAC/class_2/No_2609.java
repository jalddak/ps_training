package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2609 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nums = new int[2];
        int index = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreElements()) nums[index++] = Integer.valueOf(st.nextToken());
        System.out.println(gcd(nums[0], nums[1]));
        System.out.println(lcm(nums[0], nums[1]));
    }

    public static int gcd(int a, int b) {
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    public static int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
}
