package ps_traning.programmers.level_0;

public class 배열의_길이에_따라_다른_연산하기 {
    public int[] solution(int[] arr, int n) {
        int[] answer = {};
        int index = 0;
        if (arr.length % 2 == 0) {
            index = 1;
        }
        for (; index < arr.length; index += 2) {
            arr[index] += n;
        }
        answer = arr;
        return answer;
    }
}
