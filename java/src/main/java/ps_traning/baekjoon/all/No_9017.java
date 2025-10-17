package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_9017 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 0; tc < t; tc++) {
            int n = Integer.parseInt(br.readLine());
            int[] ranks = new int[n];
            Map<Integer, Integer> cnts = new HashMap<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                ranks[i] = Integer.parseInt(st.nextToken());
                if (!cnts.containsKey(ranks[i])) cnts.put(ranks[i], 0);
                cnts.put(ranks[i], cnts.get(ranks[i]) + 1);
            }

            Map<Integer, List<Integer>> infos = new HashMap<>();
            int score = 1;
            for (int i = 0; i < n; i++) {
                if (cnts.get(ranks[i]) != 6) continue;
                if (!infos.containsKey(ranks[i])) infos.put(ranks[i], new ArrayList<>());
                infos.get(ranks[i]).add(score++);
            }

            int result = -1;
            int temp = 200 * 1000;
            for (int num : infos.keySet()) {
                int sum = 0;
                for (int i = 0; i < 4; i++) {
                    sum += infos.get(num).get(i);
                }
                if (sum <= temp) {
                    if (sum < temp || (sum == temp && infos.get(result).get(4) > infos.get(num).get(4))) result = num;
                    temp = sum;
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}