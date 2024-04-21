package ps_traning.programmers.level_0;

public class 문자열_뒤집기_2 {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        StringBuilder sb = new StringBuilder(my_string.substring(s, e + 1));
        answer = my_string.substring(0, s) + sb.reverse().toString() + my_string.substring(e + 1);
        return answer;
    }
}
