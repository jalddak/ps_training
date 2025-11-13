package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class No_20920 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            if (input.length() < m) continue;
            if (!map.containsKey(input)) map.put(input, 0);
            map.put(input, map.get(input) + 1);
        }

        Object[][] arr = new Object[map.size()][2];
        int index = 0;
        for (String key : map.keySet()) {
            arr[index][0] = key;
            arr[index][1] = map.get(key);
            index++;
        }

        Arrays.sort(arr, (a, b) -> {
            int aCnt = (Integer) a[1];
            int bCnt = (Integer) b[1];
            String aWord = (String) a[0];
            String bWord = (String) b[0];
            if (aCnt == bCnt && aWord.length() == bWord.length()) return aWord.compareTo(bWord);
            if (aCnt == bCnt) return bWord.length() - aWord.length();
            return bCnt - aCnt;
        });

        StringBuilder sb = new StringBuilder();
        for (Object[] result : arr) {
            sb.append(result[0]).append("\n");
        }
        System.out.print(sb);
    }
}
