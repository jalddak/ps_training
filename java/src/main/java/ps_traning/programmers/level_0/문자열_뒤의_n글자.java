package ps_traning.programmers.level_0;

public class 문자열_뒤의_n글자 {
    public String solution(String my_string, int n) {
        String answer = my_string.substring(my_string.length() - n);
        return answer;
    }
}
