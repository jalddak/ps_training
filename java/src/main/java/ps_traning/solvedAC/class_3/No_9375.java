package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_9375 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            int n = Integer.valueOf(br.readLine());
            Map<String, List<String>> map = new HashMap<>();
            for (int j = 0; j < n; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String name = st.nextToken();
                String gear = st.nextToken();
                if (map.containsKey(gear)) map.get(gear).add(name);
                else map.put(gear, new ArrayList<>(List.of(name)));
            }

            int answer = 1;
            for (String gear : map.keySet()) {
                answer *= map.get(gear).size() + 1;
            }
            sb.append(answer - 1).append("\n");
        }
        System.out.print(sb.toString());
    }
}
