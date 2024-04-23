package ps_traning.programmers.level_0;

public class qr_code {
    public String solution(int q, int r, String code) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (int i = r; i < code.length(); i += q) {
            sb.append(code.charAt(i));
        }
        answer = sb.toString();
        return answer;
    }
}
