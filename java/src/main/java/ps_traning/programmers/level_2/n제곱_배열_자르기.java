package ps_traning.programmers.level_2;

public class n제곱_배열_자르기 {
    public int[] solution(int n, long left, long right) {
        int[] answer = new int[(int) (right - left + 1)];
        int i = 0;
        for (long num = left; num <= right; num++) {
            if ((int) (num / n) < num % n) {
                answer[i] = (int) (num % n + 1);
            } else {
                answer[i] = (int) (num / n + 1);
            }
            i++;
        }
        return answer;
    }
}
