package ps_traning.algostudy._250819.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_16678 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] scores = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(scores);

        long answer = 0;
        int limit = 1;
        for (int score : scores) {
            if (score < limit) continue;
            if (score != limit) answer += score - limit;
            limit++;
        }

        System.out.println(answer);
    }
}
