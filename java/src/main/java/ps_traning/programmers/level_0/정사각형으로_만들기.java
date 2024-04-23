package ps_traning.programmers.level_0;

public class 정사각형으로_만들기 {
    public int[][] solution(int[][] arr) {
        int[][] answer = {};
        int maxLen = arr.length;
        for (int i = 0; i < arr.length; i++) {
            maxLen = Math.max(maxLen, arr[i].length);
        }
        answer = new int[maxLen][maxLen];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                answer[i][j] = arr[i][j];
            }
        }
        return answer;
    }
}
