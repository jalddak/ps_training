package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = Integer.valueOf(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] scores = new int[cnt];
        int index = 0;
        int maxScore = 0;
        while (st.hasMoreTokens()) {
            int score = Integer.valueOf(st.nextToken());
            scores[index++] = score;
            if (score > maxScore) maxScore = score;
        }
        double answer = 0;
        for (int s : scores) {
            answer += (double) s / maxScore * 100;
        }

        answer /= cnt;
        System.out.println(answer);

    }
}
