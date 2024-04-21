package ps_traning.programmers.level_0;

public class 원소들의_곱과_합 {
    public int solution(int[] num_list) {
        int answer = 0;
        int sum = 0;
        int multi = 1;
        for (int n : num_list) {
            sum += n;
            multi *= n;
        }
        if (multi < sum * sum) {
            answer = 1;
        }
        return answer;
    }
}
