package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_10800 {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = Integer.parseInt(br.readLine());
        int[][] info = new int[cnt][3];

        for (int i = 0; i < cnt; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            info[i][0] = Integer.parseInt(st.nextToken());
            info[i][1] = Integer.parseInt(st.nextToken());
            info[i][2] = i;
        }

        Arrays.sort(info, (a, b) -> {
            if (a[1] == b[1]) return a[0] - b[0];
            return a[1] - b[1];
        });

        int[] recent = new int[3];
        int[] weights = new int[cnt + 1];
        int pSum = 0;
        int[] result = new int[cnt];

        for (int i = 0; i < cnt; i++) {
            int num = info[i][0], w = info[i][1], idx = info[i][2];
            result[idx] += pSum - weights[num];
            if (recent[0] == w) {
                if (recent[2] == num) result[idx] = result[info[i - 1][2]];
                else result[idx] -= recent[1] * w;
                recent[1]++;
            } else {
                recent[0] = w;
                recent[1] = 1;
            }
            recent[2] = num;
            weights[num] += w;
            pSum += w;
        }

        StringBuilder sb = new StringBuilder();
        for (int r : result) sb.append(r).append("\n");
        System.out.print(sb);
    }
}
