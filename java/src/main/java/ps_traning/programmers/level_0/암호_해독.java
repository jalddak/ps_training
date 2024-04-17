package ps_traning.programmers.level_0;

public class 암호_해독 {
    public String solution(String cipher, int code) {
        String answer = "";
        for (int i = code - 1; i < cipher.length(); i += code) {
            answer += cipher.charAt(i);
        }
        return answer;
    }
}
