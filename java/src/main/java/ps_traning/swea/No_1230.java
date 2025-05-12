package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_1230 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            int n = Integer.valueOf(br.readLine());
            List<Integer> nums = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                nums.add(Integer.valueOf(st.nextToken()));
            }
            int cmdN = Integer.valueOf(br.readLine());
            st = new StringTokenizer(br.readLine());
            List<String> cmds = new ArrayList<>();
            while (st.hasMoreTokens()) {
                cmds.add(st.nextToken());
            }
            int i = 0;
            int temp = 0;
            while (temp < cmdN) {
                if (cmds.get(i).equals("I")) {
                    i++;
                    int x = Integer.valueOf(cmds.get(i++));
                    int y = Integer.valueOf(cmds.get(i++));
                    for (int d = 0; d < y; d++) {
                        nums.add(x + d, Integer.valueOf(cmds.get(i++)));
                    }
                } else if (cmds.get(i).equals("D")) {
                    i++;
                    int x = Integer.valueOf(cmds.get(i++));
                    int y = Integer.valueOf(cmds.get(i++));
                    for (int d = 0; d < y; d++) {
                        nums.remove(x);
                    }

                } else if (cmds.get(i).equals("A")) {
                    i++;
                    int y = Integer.valueOf(cmds.get(i++));
                    for (int d = 0; d < y; d++) {
                        nums.add(Integer.valueOf(cmds.get(i++)));
                    }
                }
                temp++;
            }
            for (i = 0; i < 10; i++) {
                sb.append(nums.get(i)).append(" ");
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}
