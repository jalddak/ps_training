package ps_traning.programmers.level_0;

public class 문자열이_몇_번_등장하는지_세기 {
    public int solution(String myString, String pat) {
        int answer = 0;
        for (int i = 0; i + pat.length() <= myString.length(); i++) {
            if (myString.substring(i, i + pat.length()).equals(pat)) {
                answer += 1;
            }
        }
        return answer;
    }
}
