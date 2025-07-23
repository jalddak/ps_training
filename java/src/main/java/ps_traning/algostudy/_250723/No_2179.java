package ps_traning.algostudy._250723;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_2179 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        List<String> words = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            words.add(br.readLine());
        }

        Map<String, List<String>> map = new HashMap<>();
        map.put("", words);
        Set<String> candidates = new HashSet<>();

        int index = 0;
        int maxLen = 0;
        while (!map.isEmpty()) {
            Map<String, List<String>> nMap = new HashMap<>();

            boolean flag = true;
            for (String key : map.keySet()) {
                List<String> values = map.get(key);
                if (values.size() >= 2) {
                    if (flag) {
                        candidates = new HashSet<>();
                        maxLen = key.length();
                        flag = false;
                    }
                    candidates.add(values.get(0));
                    candidates.add(values.get(1));
                }
                for (String word : values) {
                    if (index >= word.length()) continue;
                    String ch = String.valueOf(word.charAt(index));
                    if (!nMap.containsKey(key + ch)) nMap.put(key + ch, new ArrayList<>());
                    nMap.get(key + ch).add(word);
                }
            }
            map = nMap;
            index++;
        }

        String s = "", t = "";
        boolean flag = true;
        for (int i = 0; i < n; i++) {
            String word = words.get(i);
            if (flag && candidates.contains(word)) {
                s = word;
                flag = false;
                continue;
            }

            int compareLen = Math.min(word.length(), s.length());
            int len = 0;
            for (int j = 0; j < compareLen; j++) {
                if (word.charAt(j) != s.charAt(j)) break;
                len += 1;
            }
            if (len != maxLen) continue;
            t = word;
            break;
        }

        System.out.println(s);
        System.out.println(t);

    }
}
