package ps_traning.programmers.level_2;

public class 카펫 {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        for (int c = 1; c <= (int) Math.sqrt(yellow); c++) {
            if (yellow % c != 0) {
                continue;
            }
            int r = yellow / c;
            if (r * 2 + c * 2 + 4 == brown) {
                answer = new int[]{r + 2, c + 2};
                break;
            }
        }
        return answer;
    }
}
