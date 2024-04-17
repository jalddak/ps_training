package ps_traning.programmers.level_0;

public class 자릿수_더하기 {
    public int solution(int n) {
        int answer = 0;
        String str = String.valueOf(n);
        for (String num : str.split("")) {
            answer += Integer.valueOf(num);
        }
        return answer;
    }
}
