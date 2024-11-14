package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_11727 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        List<Integer> dp = new ArrayList<>(List.of(0, 1, 3));
        for (int i = 3; i <= n; i++) {
            dp.add((dp.get(i - 1) + dp.get(i - 2) * 2) % 10007);
        }
        System.out.println(dp.get(n));
    }
}
