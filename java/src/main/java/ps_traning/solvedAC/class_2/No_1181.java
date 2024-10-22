package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1181 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        List<String>[] lenArr = new ArrayList[51];
        for (int i = 0; i < 51; i++) {
            lenArr[i] = new ArrayList<>();
        }

        Set<String> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            set.add(br.readLine());
        }
        List<String> list = new ArrayList<>(set);
        for (String s : list) {
            int len = s.length();
            lenArr[len].add(s);
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 51; i++) {
            List<String> temp = lenArr[i];
            if (temp.isEmpty()) continue;
            Collections.sort(temp);
            for (String s : temp) {
                sb.append(s + '\n');
            }
        }
        System.out.println(sb.toString());
    }
}
