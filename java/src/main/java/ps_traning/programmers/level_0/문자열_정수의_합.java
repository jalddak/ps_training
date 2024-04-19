package ps_traning.programmers.level_0;

public class 문자열_정수의_합 {
    public int solution(String num_str) {
        int answer = 0;
        for (String n_str : num_str.split("")) {
            answer += Integer.valueOf(n_str);
        }
        return answer;
    }
}
