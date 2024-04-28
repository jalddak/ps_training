package ps_traning.programmers.level_1;

public class 푸드_파이터_대회 {
    public String solution(int[] food) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < food.length; i++) {
            for (int n = 0; n < (int) food[i] / 2; n++) {
                sb.append(i);
            }
        }
        String half = sb.toString();
        String reversed = sb.reverse().toString();
        sb.setLength(0);
        sb.append(half);
        sb.append(0);
        sb.append(reversed);
        answer = sb.toString();
        return answer;
    }
}
