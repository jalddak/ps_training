package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_27172_useOnlyArr {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        int[] cnts = new int[1000001];
        boolean[] checked = new boolean[1000001];

        for (int i = 0; i < n; i++) {
            int num = Integer.valueOf(st.nextToken());
            nums[i] = num;
            checked[num] = true;
        }

        for (int num : nums) {
            for (int target = num * 2; target <= 1000000; target += num) {
                if (!checked[target]) continue;
                cnts[num] += 1;
                cnts[target] -= 1;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int num : nums) {
            sb.append(cnts[num]).append(" ");
        }

        System.out.println(sb.toString());
    }
}
