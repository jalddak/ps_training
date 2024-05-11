package ps_traning.programmers.level_3;

import java.util.Arrays;

public class 정수_삼각형 {
    public int solution(int[][] triangle) {
        int answer = 0;
        int[] dp = {0};
        for (int[] row : triangle) {
            int[] temp = new int[row.length];

            for (int i = 0; i < row.length; i++) {
                if (i == 0) {
                    temp[i] = dp[i] + row[i];
                } else if (i == row.length - 1) {
                    temp[i] = dp[i - 1] + row[i];
                } else {
                    temp[i] = Math.max(dp[i], dp[i - 1]) + row[i];
                }
            }

            dp = temp;
        }
        Arrays.sort(dp);
        answer = dp[dp.length - 1];
        return answer;
    }
}
