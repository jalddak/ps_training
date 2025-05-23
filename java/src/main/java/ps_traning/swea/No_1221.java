package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class No_1221 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] snums = {"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"};
        Map<String, Integer> stoi = new HashMap<>();
        Map<Integer, String> itos = new HashMap<>();
        for (int i = 0; i < 10; i++) {
            stoi.put(snums[i], i);
            itos.put(i, snums[i]);
        }

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String pre = st.nextToken();
            int n = Integer.valueOf(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                nums[i] = stoi.get(st.nextToken());
            }
            Arrays.sort(nums);
            StringBuilder result = new StringBuilder();
            for (int num : nums) {
                result.append(itos.get(num)).append(" ");
            }

            sb.append(pre).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
