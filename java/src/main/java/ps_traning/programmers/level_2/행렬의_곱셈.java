package ps_traning.programmers.level_2;

public class 행렬의_곱셈 {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int rowLen = arr1.length;
        int colLen = arr2[0].length;
        int mix = arr2.length;
        int[][] answer = new int[rowLen][colLen];
        for (int i = 0; i < rowLen; i++) {
            for (int j = 0; j < colLen; j++) {
                int result = 0;
                for (int k = 0; k < mix; k++) {
                    result += arr1[i][k] * arr2[k][j];
                }
                answer[i][j] = result;
            }
        }
        return answer;
    }
}
