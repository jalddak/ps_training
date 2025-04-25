package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_17404 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[][] costs = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                costs[i][j] = Integer.valueOf(st.nextToken());
            }
        }

        int inf = 1000 * 1000 + 1;
        Stack<int[][]> dp = new Stack<>();
        dp.push(new int[][]{
                {inf, costs[0][1] + costs[1][0], costs[0][2] + costs[1][0]},
                {costs[0][0] + costs[1][1], inf, costs[0][2] + costs[1][1]},
                {costs[0][0] + costs[1][2], costs[0][1] + costs[1][2], inf}
        });

        for (int i = 2; i < n; i++) {
            int[][] before = dp.pop();
            int[][] next = new int[3][3];

            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    List<Integer> minCheck = new ArrayList<>();
                    for (int a = 0; a < 3; a++) {
                        if (j == a) continue;
                        minCheck.add(before[a][k]);
                    }
//                    next[j][k] = minCheck.stream().min(Integer::compareTo).get();
                    next[j][k] = Collections.min(minCheck) + costs[i][j];
                }
            }
            dp.push(next);
        }

        int[][] last = dp.pop();
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == j) continue;
                result.add(last[i][j]);
            }
        }

        int answer = Collections.min(result);
        System.out.println(answer);
    }
}
