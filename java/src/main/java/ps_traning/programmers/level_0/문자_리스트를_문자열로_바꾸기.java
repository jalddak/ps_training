package ps_traning.programmers.level_0;

public class 문자_리스트를_문자열로_바꾸기 {
    public String solution(String[] arr) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (String str : arr) {
            sb.append(str);
        }
        answer = sb.toString();
        return answer;
    }
}
