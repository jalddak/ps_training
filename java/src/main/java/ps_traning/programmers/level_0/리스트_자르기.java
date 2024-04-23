package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 리스트_자르기 {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = {};
        if (n == 1) {
            answer = Arrays.copyOfRange(num_list, 0, slicer[1] + 1);
        } else if (n == 2) {
            answer = Arrays.copyOfRange(num_list, slicer[0], num_list.length);
        } else if (n == 3) {
            answer = Arrays.copyOfRange(num_list, slicer[0], slicer[1] + 1);
        } else if (n == 4) {
            answer = new int[num_list.length];
            int index = 0;
            for (int i = slicer[0]; i <= slicer[1]; i += slicer[2]) {
                answer[index] = num_list[i];
                index++;
            }
            answer = Arrays.copyOfRange(answer, 0, index);
        }
        return answer;
    }
}
