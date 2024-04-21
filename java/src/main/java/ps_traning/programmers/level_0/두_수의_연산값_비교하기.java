package ps_traning.programmers.level_0;

public class 두_수의_연산값_비교하기 {
    public int solution(int a, int b) {
        int answer = Math.max(Integer.valueOf(String.valueOf(a) + String.valueOf(b)), 2 * a * b);

        return answer;
    }
}
