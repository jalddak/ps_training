package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_10952 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            int[] nums = new int[2];
            int index = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) nums[index++] = Integer.valueOf(st.nextToken());
            if (nums[0] == 0 && nums[1] == 0) break;
            System.out.println(nums[0] + nums[1]);
        }
    }
}
