package ps_traning.programmers.level_3;

public class 등굣깃 {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] board = new int[n + 1][m + 1];
        board[1][1] = 1;
        for (int i = 0; i < puddles.length; i++) {
            board[puddles[i][1]][puddles[i][0]] = -1;
        }
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (i == 1 && j == 1) continue;
                if (board[i][j] == -1) {
                    board[i][j] = 0;
                    continue;
                }
                board[i][j] = board[i - 1][j] + board[i][j - 1];
            }
        }

        answer = board[n][m];
        return answer;
    }
}
