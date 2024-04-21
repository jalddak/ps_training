package ps_traning.programmers.level_0;

public class 접미사인지_확인하기 {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        int index = my_string.lastIndexOf(is_suffix);
        if (index != -1 && index + is_suffix.length() == my_string.length()) {
            answer = 1;
        }
        return answer;
    }
}
