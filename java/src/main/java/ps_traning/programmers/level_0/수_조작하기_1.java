package ps_traning.programmers.level_0;

public class 수_조작하기_1 {
    public int solution(int n, String control) {
        int answer = n;
        for (char c : control.toCharArray()) {
            if (c == 'w') {
                answer += 1;
            } else if (c == 's') {
                answer -= 1;
            } else if (c == 'd') {
                answer += 10;
            } else if (c == 'a') {
                answer -= 10;
            }
        }
        return answer;
    }
}
