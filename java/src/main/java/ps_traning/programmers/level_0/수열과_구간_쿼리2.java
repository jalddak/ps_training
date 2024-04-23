package ps_traning.programmers.level_0;

public class 수열과_구간_쿼리2 {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        int index = 0;
        for (int[] query : queries) {
            int result = -1;
            for (int i = query[0]; i <= query[1]; i++) {
                if (arr[i] > query[2]) {
                    if (result == -1) {
                        result = arr[i];
                    } else {
                        result = Math.min(result, arr[i]);
                    }
                }
            }
            answer[index] = result;
            index++;
        }
        return answer;
    }
}
