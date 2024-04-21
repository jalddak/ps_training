package ps_traning.programmers.level_0;

public class 홀수_vs_짝수 {
    public int solution(int[] num_list) {
        int answer = 0;
        int oddSum = 0;
        int evenSum = 0;
        for (int i = 0; i < num_list.length; i++) {
            if (i % 2 == 0) {
                oddSum += num_list[i];
            } else {
                evenSum += num_list[i];
            }
        }
        answer = Math.max(oddSum, evenSum);
        return answer;
    }
}
