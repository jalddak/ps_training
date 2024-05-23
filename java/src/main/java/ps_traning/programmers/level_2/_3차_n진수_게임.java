package ps_traning.programmers.level_2;

public class _3차_n진수_게임 {
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        int len = t * m;
        StringBuilder sb = new StringBuilder();
        int num = 0;
        while (len > sb.length()) {
            sb.append(Integer.toString(num++, n).toUpperCase());
        }
        StringBuilder ab = new StringBuilder();
        for (int i = p - 1; ab.length() < t; i += m) {
            ab.append(sb.charAt(i));
        }
        answer = ab.toString();
        return answer;
    }
}
