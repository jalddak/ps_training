package ps_traning.programmers.level_0;

public class 카운트_업 {
    public int[] solution(int start_num, int end_num) {
        int[] answer = new int[end_num - start_num + 1];
        int index = 0;
        for (int num = start_num; num <= end_num; num++) {
            answer[index] = num;
            index++;
        }
        return answer;
    }
}
