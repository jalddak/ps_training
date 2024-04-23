package ps_traning.programmers.level_0;

public class 문자열_겹쳐쓰기 {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        int len = overwrite_string.length();
        StringBuilder sb = new StringBuilder(my_string);
        sb.replace(s, s + len, overwrite_string);
        answer = sb.toString();
        return answer;
    }
}
