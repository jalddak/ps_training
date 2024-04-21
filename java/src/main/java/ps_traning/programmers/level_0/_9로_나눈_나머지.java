package ps_traning.programmers.level_0;

public class _9로_나눈_나머지 {
    public int solution(String number) {
        int answer = 0;
        for (String s : number.split("")) {
            answer += Integer.valueOf(s);
        }
        answer %= 9;
        return answer;
    }
}
