package ps_traning.programmers.level_0;

public class 수열과_구간_쿼리_1 {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        for (int[] query : queries) {
            for (int i = query[0]; i < query[1] + 1; i++) {
                arr[i] += 1;
            }
        }
        answer = arr;
        return answer;
    }
}
