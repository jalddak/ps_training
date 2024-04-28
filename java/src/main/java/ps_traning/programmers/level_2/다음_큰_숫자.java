package ps_traning.programmers.level_2;

public class 다음_큰_숫자 {
    public int count1(int n) {
        int cnt = 0;
        String binN = Integer.toString(n, 2);
        for (char c : binN.toCharArray()) {
            if (c == '1') {
                cnt++;
            }
        }
        return cnt;
    }

    public int solution(int n) {
        int cnt = count1(n);
        while (true) {
            n++;
            if (cnt == count1(n)) {
                break;
            }
        }
        return n;
    }
}
