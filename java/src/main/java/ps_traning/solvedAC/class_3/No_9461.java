package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_9461 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            List<Long> dp = new ArrayList<>(List.of(0L, 1L, 1L, 1L, 2L, 2L, 3L, 4L, 5L, 7L, 9L));
            int n = Integer.valueOf(br.readLine());
            for (int j = 10; j < n; j++) {
                dp.add(dp.get(j) + dp.get(j - 4));
            }
            sb.append(dp.get(n)).append("\n");
        }
        System.out.print(sb.toString());
    }
}
