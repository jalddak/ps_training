package ps_traning.programmers.level_1;

public class 핸드폰_번호_가리기 {
    public String solution(String phone_number) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < phone_number.length() - 4; i++) {
            sb.append("*");
        }
        sb.append(phone_number.substring(phone_number.length() - 4, phone_number.length()));
        answer = sb.toString();
        return answer;
    }
}
