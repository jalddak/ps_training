package ps_traning.programmers.level_0;

public class _0_떼기 {
    public String solution(String n_str) {
        String answer = "";
        int start = 0;
        for (int i = 0; i < n_str.length(); i++) {
            char c = n_str.charAt(i);
            if (c != '0') {
                start = i;
                break;
            }
        }
        answer = n_str.substring(start);
        return answer;
    }
}
