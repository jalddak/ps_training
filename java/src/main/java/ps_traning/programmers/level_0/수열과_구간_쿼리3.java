package ps_traning.programmers.level_0;

public class 수열과_구간_쿼리3 {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        for (int[] query : queries) {
            int i = query[0], j = query[1];
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        answer = arr;
        return answer;
    }
}
