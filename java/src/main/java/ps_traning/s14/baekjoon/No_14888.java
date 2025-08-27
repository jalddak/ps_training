package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_14888 {

    private static int n, maxR, minR;
    private static int[] nums;
    private static int[] cnts = new int[4];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        nums = new int[n];
        maxR = Integer.MIN_VALUE;
        minR = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            cnts[i] = Integer.parseInt(st.nextToken());
        }

        recursion(0, nums[0]);
        System.out.println(maxR);
        System.out.println(minR);
    }

    private static void recursion(int depth, int num) {
        if (depth == n - 1) {
            maxR = Math.max(maxR, num);
            minR = Math.min(minR, num);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (cnts[i] == 0) continue;
            int nNum = calc(i, num, nums[depth + 1]);
            cnts[i] -= 1;
            recursion(depth + 1, nNum);
            cnts[i] += 1;
        }
    }

    private static int calc(int idx, int a, int b) {
        switch (idx) {
            case 0:
                a += b;
                break;
            case 1:
                a -= b;
                break;
            case 2:
                a *= b;
                break;
            case 3:
                a /= b;
                break;
        }
        return a;
    }
}
