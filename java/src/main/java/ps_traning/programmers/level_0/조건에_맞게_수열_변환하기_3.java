package ps_traning.programmers.level_0;

public class 조건에_맞게_수열_변환하기_3 {
    public int[] solution(int[] arr, int k) {
        int[] answer = {};
        for (int i = 0; i < arr.length; i++) {
            if (k % 2 == 1) {
                arr[i] *= k;
            } else {
                arr[i] += k;
            }
        }
        answer = arr;
        return answer;
    }
}
