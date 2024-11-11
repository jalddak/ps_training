package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_9095 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        int[] ns = new int[t];
        int maxN = 0;
        for (int i = 0; i < t; i++) {
            int n = Integer.valueOf(br.readLine());
            ns[i] = n;
            maxN = Math.max(maxN, n);
        }

        List<Integer> dp = new ArrayList<>(List.of(0, 1, 2, 4));
        for (int i = 4; i <= maxN; i++) {
            dp.add(dp.get(i - 1) + dp.get(i - 2) + dp.get(i - 3));
        }

        StringBuilder sb = new StringBuilder();
        for (int n : ns) {
            sb.append(dp.get(n)).append("\n");
        }
        System.out.print(sb.toString());
    }
}
