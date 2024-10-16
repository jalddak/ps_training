package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_10871 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] cmds = new int[2];
        int index = 0;
        while (st.hasMoreTokens()) cmds[index++] = Integer.valueOf(st.nextToken());
        st = new StringTokenizer(br.readLine());
        List<Integer> nums = new ArrayList<>();
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            if (num < cmds[1]) nums.add(num);
        }
        StringBuilder sb = new StringBuilder();
        for (int n : nums) {
            sb.append(n + " ");
        }
        System.out.println(sb.toString());

    }
}
