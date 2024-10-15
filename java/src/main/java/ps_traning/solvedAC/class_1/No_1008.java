package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1008 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[2];
        int index = 0;
        while (st.hasMoreTokens()) {
            nums[index++] = Integer.parseInt(st.nextToken());
        }
        double answer = (double) nums[0] / nums[1];
        System.out.println(answer);
    }
}
