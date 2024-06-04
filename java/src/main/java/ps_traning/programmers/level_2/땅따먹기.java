package ps_traning.programmers.level_2;

public class 땅따먹기 {
    int solution(int[][] land) {
        int answer = 0;
        int[] dp = land[0];
        for (int i = 1; i < land.length; i++) {
            int[] ndp = new int[4];
            for (int j = 0; j < 4; j++) {
                int maxScore = 0;
                for (int k = 0; k < 4; k++) {
                    if (k == j) continue;
                    int score = dp[k];
                    maxScore = Math.max(maxScore, score);
                }
                ndp[j] = maxScore + land[i][j];
            }
            dp = ndp;
        }
        for (int score : dp) answer = Math.max(answer, score);

        return answer;
    }
}
