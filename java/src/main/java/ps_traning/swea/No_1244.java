package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1244 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int c = 1; c <= t; c++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String num = st.nextToken();
            int cnt = Integer.valueOf(st.nextToken());
            int numLen = num.length();
            String result = "";

            Stack<String> stack = new Stack<>();
            stack.push(num);

            for (int a = 0; a < cnt; a++) {
                Set<String> set = new HashSet<>();
                while (!stack.isEmpty()) {
                    String temp = stack.pop();
                    for (int i = 0; i < numLen; i++) {
                        for (int j = i + 1; j < numLen; j++) {
                            char[] candidate = temp.toCharArray();
                            candidate[i] = temp.charAt(j);
                            candidate[j] = temp.charAt(i);
                            set.add(String.valueOf(candidate));
                        }
                    }
                }
                stack.addAll(set);
            }
            result = stack.stream().max(Comparator.naturalOrder()).get();
            sb.append("#").append(c).append(" ").append(result).append("\n");
        }
        System.out.print(sb.toString());
    }
}
