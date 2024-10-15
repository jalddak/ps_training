package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_10250 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] nums = new int[3];
            int index = 0;
            while (st.hasMoreTokens()) nums[index++] = Integer.valueOf(st.nextToken());
            int h = nums[0], w = nums[1], n = nums[2];
            boolean flag = (n % h == 0) ? true : false;
            int floor = n % h + ((flag) ? h : 0);
            int roomNum = 1 + n / h - ((flag ? 1 : 0));
            String srn = (roomNum < 10) ? "0" + roomNum : String.valueOf(roomNum);
            System.out.println(floor + srn);
        }
    }
}
