package ps_traning.programmers.level_0;

public class 특정_문자열로_끝나는_가장_긴_부분_문자열_찾기 {
    public String solution(String myString, String pat) {
        String answer = "";
        int li = myString.lastIndexOf(pat);
        answer = myString.substring(0, li + pat.length());
        return answer;
    }
}
