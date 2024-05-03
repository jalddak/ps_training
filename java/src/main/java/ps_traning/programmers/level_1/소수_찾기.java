package ps_traning.programmers.level_1;

public class 소수_찾기 {
    public int solution(int n) {
        int answer = 0;
        boolean[] checked = new boolean[n + 1];
        for (int num = 2; num <= n; num++) {
            if (checked[num]) continue;
            answer++;
            for (int m = num; m <= n; m += num) {
                checked[m] = true;
            }
        }
        return answer;
    }
}
