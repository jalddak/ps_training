package ps_traning.programmers.level_1;

public class 크기가_작은_부분_문자열 {
    public int solution(String t, String p) {
        int answer = 0;
        int tLen = t.length();
        int pLen = p.length();
        long intP = Long.valueOf(p);
        for (int i = 0; i < tLen - pLen + 1; i++) {
            long subN = Long.valueOf(t.substring(i, i + pLen));
            if (subN <= intP) {
                answer++;
            }
        }
        return answer;
    }
}
