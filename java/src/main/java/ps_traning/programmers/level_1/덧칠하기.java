package ps_traning.programmers.level_1;

public class 덧칠하기 {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int cover = 0;
        for (int s : section) {
            if (cover < s) {
                cover = s + m - 1;
                answer++;
            }
        }
        return answer;
    }
}
