package ps_traning.programmers.level_0;

public class 두_수의_합2 {
    public String solution(String a, String b) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        StringBuilder asb = new StringBuilder(a);
        StringBuilder bsb = new StringBuilder(b);
        asb = asb.reverse();
        bsb = bsb.reverse();
        int up = 0;
        for (int i = 0; i < Math.max(a.length(), b.length()); i++) {
            int an = 0;
            int bn = 0;
            if (i < a.length()) {
                an = asb.charAt(i) - '0';
            }
            if (i < b.length()) {
                bn = bsb.charAt(i) - '0';
            }
            int sum = (an + bn + up) % 10;
            sb.append(sum);
            up = (an + bn + up) / 10;
        }
        if (up != 0) {
            sb.append(up);
        }
        sb = sb.reverse();
        answer = sb.toString();
        return answer;
    }
}
