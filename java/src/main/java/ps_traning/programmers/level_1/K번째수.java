package ps_traning.programmers.level_1;

import java.util.Arrays;

public class K번째수 {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++) {
            int[] command = commands[i];
            int[] select = Arrays.copyOfRange(array, command[0] - 1, command[1]);
            Arrays.sort(select);
            answer[i] = select[command[2] - 1];
        }
        return answer;
    }
}
