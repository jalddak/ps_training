package ps_traning.programmers.level_0;

public class 숨어있는_숫자의_덧셈_1 {
    public int solution(String my_string) {
        int answer = 0;
        for (String s : my_string.split("")) {
            try {
                answer += Integer.valueOf(s);
            } catch (Exception e) {
                continue;
            }
        }
        return answer;
    }
}
