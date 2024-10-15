package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class No_2675 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            StringBuilder sb = new StringBuilder();
            ArrayList<Object> list = new ArrayList<>();
            while (st.hasMoreTokens()) list.add(st.nextToken());
            int it = Integer.valueOf((String) list.get(0));
            String cmd = (String) list.get(1);
            for (char c : cmd.toCharArray()) {
                for (int j = 0; j < it; j++) sb.append(c);
            }
            System.out.println(sb.toString());
        }
    }
}
