package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class No_1620 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        StringBuilder sb = new StringBuilder();
        Map<Integer, String> iTN = new HashMap<>();
        Map<String, Integer> nTI = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            String name = br.readLine();
            iTN.put(i, name);
            nTI.put(name, i);
        }
        for (int i = 0; i < m; i++) {
            String input = br.readLine();
            if (Character.isDigit(input.charAt(0))) sb.append(iTN.get(Integer.valueOf(input))).append("\n");
            else sb.append(nTI.get(input)).append("\n");
        }
        System.out.print(sb.toString());
    }
}
