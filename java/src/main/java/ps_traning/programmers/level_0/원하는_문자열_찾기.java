package ps_traning.programmers.level_0;

public class 원하는_문자열_찾기 {
    public int solution(String myString, String pat) {
        int answer = 0;
        myString = myString.toLowerCase();
        pat = pat.toLowerCase();
        if (myString.contains(pat)) {
            answer = 1;
        }
        return answer;
    }
}
