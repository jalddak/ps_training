package ps_traning.programmers.level_0;

public class 대문자와_소문자 {
    public String solution(String my_string) {
        String answer = "";
        for (char alphabet : my_string.toCharArray()) {
            if (Character.isUpperCase(alphabet)) {
                answer += Character.toLowerCase(alphabet);
            } else {
                answer += Character.toUpperCase(alphabet);
            }
        }
        return answer;
    }
}
