package ps_traning.programmers.level_0;

public class 접두사인지_확인하기 {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
        if (my_string.indexOf(is_prefix) == 0) {
            answer = 1;
        }
        return answer;
    }
}
