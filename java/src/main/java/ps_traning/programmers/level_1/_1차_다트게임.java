package ps_traning.programmers.level_1;

public class _1차_다트게임 {
    public int solution(String dartResult) {
        int answer = 0;
        int[] scores = new int[3];
        int index = 0;
        StringBuilder num = new StringBuilder();
        for (char c : dartResult.toCharArray()) {
            if (Character.isDigit(c)) {
                num.append(c);
                continue;
            }
            if (num.length() != 0) {
                scores[index] = Integer.valueOf(num.toString());
                index++;
                num.setLength(0);
            }
            if (c == 'D') {
                scores[index - 1] = (int) Math.pow(scores[index - 1], 2);
            }
            if (c == 'T') {
                scores[index - 1] = (int) Math.pow(scores[index - 1], 3);
            }
            if (c == '*') {
                scores[index - 1] *= 2;
                if (index > 1) scores[index - 2] *= 2;
            }
            if (c == '#') {
                scores[index - 1] = -scores[index - 1];
            }
        }
        for (int n : scores) {
            answer += n;
        }
        return answer;
    }
}
