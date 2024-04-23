package ps_traning.programmers.level_0;

public class 조건_문자열 {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        if (ineq.equals(">") && eq.equals("=") && n >= m) {
            answer = 1;
        }
        if (ineq.equals("<") && eq.equals("=") && n <= m) {
            answer = 1;
        }
        if (ineq.equals(">") && eq.equals("!") && n > m) {
            answer = 1;
        }
        if (ineq.equals("<") && eq.equals("!") && n < m) {
            answer = 1;
        }
        return answer;
    }
}
