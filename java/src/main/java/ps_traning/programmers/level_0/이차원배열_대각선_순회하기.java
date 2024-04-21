package ps_traning.programmers.level_0;

public class 이차원배열_대각선_순회하기 {
    public int solution(int[][] board, int k) {
        int answer = 0;
        int r = board.length, c = board[0].length;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (i + j <= k) {
                    answer += board[i][j];
                }
            }
        }
        return answer;
    }
}
