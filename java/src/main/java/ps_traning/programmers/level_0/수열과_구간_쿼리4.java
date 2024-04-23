package ps_traning.programmers.level_0;

public class 수열과_구간_쿼리4 {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        for (int[] query : queries) {
            for (int i = query[0]; i <= query[1]; i++) {
                if (i % query[2] == 0) {
                    arr[i]++;
                }
            }
        }
        answer = arr;
        return answer;
    }
}
