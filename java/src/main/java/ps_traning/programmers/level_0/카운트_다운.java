package ps_traning.programmers.level_0;

public class 카운트_다운 {
    public int[] solution(int start, int end_num) {
        int[] answer = new int[start - end_num + 1];
        int index = 0;
        for (int num = start; num >= end_num; num--) {
            answer[index] = num;
            index++;
        }
        return answer;
    }
}
