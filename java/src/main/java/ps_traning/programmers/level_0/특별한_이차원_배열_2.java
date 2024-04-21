package ps_traning.programmers.level_0;

public class 특별한_이차원_배열_2 {
    public int solution(int[][] arr) {
        int answer = 1;
        int len = arr.length;
        Loop:
        for (int i = 0; i < len; i++) {
            for (int j = i; j < len; j++) {
                if (arr[i][j] != arr[j][i]) {
                    answer = 0;
                    break Loop;
                }
            }
        }
        return answer;
    }
}
