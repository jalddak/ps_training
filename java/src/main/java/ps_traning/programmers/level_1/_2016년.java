package ps_traning.programmers.level_1;

public class _2016년 {
    public String solution(int a, int b) {
        String answer = "";

        int[] months = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30};
        String[] weeks = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};
        int days = b;
        for (int i = 1; i < a; i++) {
            days += months[i];
        }
        answer = weeks[days % 7];
        return answer;
    }
}
