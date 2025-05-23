package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1233 {
    private static Set<String> set = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int tcCnt = 10;
        set.add("+");
        set.add("*");
        set.add("/");
        set.add("-");

        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());
            int result = 1;
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                List<String> temp = new ArrayList<>();
                while (st.hasMoreTokens()) temp.add(st.nextToken());
                if ((temp.size() == 2 && set.contains(temp.get(1))) || (temp.size() == 4) && !set.contains(temp.get(1))) {
                    result = 0;
                }
            }

            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
