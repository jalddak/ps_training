package ps_traning.programmers.level_0;

public class 조건에_맞게_수열_변환하기_1 {
    public int[] solution(int[] arr) {
        int[] answer = {};
        for (int i = 0; i < arr.length; i++) {
            int n = arr[i];
            if (n >= 50 && n % 2 == 0) {
                arr[i] = n / 2;
            } else if (n < 50 && n % 2 != 0) {
                arr[i] = n * 2;
            }
        }
        answer = arr;
        return answer;
    }
}
