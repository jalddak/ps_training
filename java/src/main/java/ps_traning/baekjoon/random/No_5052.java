package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class No_5052 {

    private static int n;
    private static Map<String, Set<String>> map;
    private static Set<String> numbers;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            n = Integer.valueOf(br.readLine());
            map = new HashMap<>();
            for (int j = 0; j < n; j++) {
                if (map.isEmpty()) map.put("", new HashSet<>());
                map.get("").add(br.readLine());
            }
            numbers = map.get("");
            sb.append(logic()).append("\n");
        }
        System.out.print(sb);
    }

    private static String logic() {

        String result = "YES";
        int index = 0;
        while (!map.isEmpty()) {
            Map<String, Set<String>> temp = new HashMap<>();

            for (String key : map.keySet()) {
                Set<String> value = map.get(key);
                if (numbers.contains(key) && value.size() > 1) {
                    result = "NO";
                    return result;
                }
                for (String num : value) {
                    if (index >= num.length()) continue;
                    String part = String.valueOf(num.charAt(index));
                    String nKey = key + part;
                    if (!temp.containsKey(nKey)) temp.put(nKey, new HashSet<>());
                    temp.get(nKey).add(num);
                }
            }
            map = temp;
            index++;

        }
        return result;
    }
}
