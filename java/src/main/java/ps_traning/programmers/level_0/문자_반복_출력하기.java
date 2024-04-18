package ps_traning.programmers.level_0;

public class 문자_반복_출력하기 {
    public String solution(String my_string, int n) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (char alphabet : my_string.toCharArray()) {
            for (int i = 0; i < n; i++) {
                sb.append(alphabet);
            }
        }
        answer = sb.toString();
        return answer;
    }
}
