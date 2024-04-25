package ps_traning.programmers.level_1;

public class _3진법_뒤집기 {
    public int solution(int n) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        while (n >= 3) {
            sb.append(n % 3);
            n /= 3;
        }
        sb.append(n);
        sb = sb.reverse();
        for (int i = 0; i < sb.length(); i++) {
            int num = sb.charAt(i) - '0';
            answer += num * Math.pow(3, i);
        }
        return answer;
    }
}
