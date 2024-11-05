package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_11723_2 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[] check = new int[21];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            int num = 0;
            if (st.hasMoreTokens()) num = Integer.parseInt(st.nextToken());

            if (cmd.equals("add")) check[num] = 1;
            else if (cmd.equals("remove")) check[num] = 0;
            else if (cmd.equals("check")) sb.append(check[num]).append("\n");
            else if (cmd.equals("toggle")) check[num] = check[num] == 1 ? 0 : 1;
            else if (cmd.equals("all")) {
                for (int j = 1; j <= 20; j++) check[j] = 1;
            } else if (cmd.equals("empty")) {
                for (int j = 1; j <= 20; j++) check[j] = 0;
            }
        }
        System.out.print(sb.toString());
    }
}
