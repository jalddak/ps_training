package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class No_11723 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        Set<Integer> set = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            int num = 0;
            if (st.hasMoreTokens()) num = Integer.parseInt(st.nextToken());

            if (cmd.equals("add")) set.add(num);
            else if (cmd.equals("remove") && set.contains(num)) set.remove(num);
            else if (cmd.equals("check")) sb.append(set.contains(num) ? 1 : 0).append("\n");
            else if (cmd.equals("toggle")) {
                if (set.contains(num)) set.remove(num);
                else set.add(num);
            } else if (cmd.equals("all")) {
                for (int j = 1; j <= 20; j++) set.add(j);
            } else if (cmd.equals("empty")) set.clear();
        }
        System.out.print(sb.toString());
    }
}
