package ps_traning.programmers.level_0;

public class 문자열_바꿔서_찾기 {
    public int solution(String myString, String pat) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        for (char c : myString.toCharArray()) {
            if (c == 'A') {
                sb.append('B');
            } else {
                sb.append('A');
            }
        }
        String change = sb.toString();
        if (change.contains(pat)) {
            answer = 1;
        }
        return answer;
    }
}
