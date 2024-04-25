package ps_traning.programmers.level_1;

public class 문자열_다루기_기본 {
    public boolean solution(String s) {
        boolean answer = true;
        if (s.length() != 4 && s.length() != 6) {
            answer = false;
        } else {
            try {
                Integer.valueOf(s);
            } catch (Exception e) {
                answer = false;
            }
        }
        return answer;
    }
}
