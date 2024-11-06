package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class No_11047 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int k = Integer.valueOf(st.nextToken());
        List<Integer> coins = new ArrayList<>();
        for (int i = 0; i < n; i++) coins.add(Integer.valueOf(br.readLine()));
        coins.sort(Collections.reverseOrder());
        int answer = 0;
        for (int c : coins) {
            answer += k / c;
            k %= c;
        }
        System.out.println(answer);
    }
}
