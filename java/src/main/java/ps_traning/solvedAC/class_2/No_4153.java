package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class No_4153 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception {
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            List<Integer> lengths = new ArrayList<>();
            boolean flag = true;
            while (st.hasMoreTokens()) {
                int num = Integer.parseInt(st.nextToken());
                if (num != 0) flag = false;
                lengths.add(num);
            }
            if (flag) break;
            Collections.sort(lengths);
            if (Math.pow(lengths.get(0), 2) + Math.pow(lengths.get(1), 2) == Math.pow(lengths.get(2), 2)) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }

    }
}
