package ps_traning.programmers.level_0;

public class 특별한_이차원_배열_1 {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) answer[i][j] = 1;
            }
        }
        return answer;
    }
}
