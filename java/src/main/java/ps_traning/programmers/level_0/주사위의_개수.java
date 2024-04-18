package ps_traning.programmers.level_0;

public class 주사위의_개수 {
    public int solution(int[] box, int n) {
        int answer = (int) (box[0] / n) * (int) (box[1] / n) * (int) (box[2] / n);
        return answer;
    }
}
