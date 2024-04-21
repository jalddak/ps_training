package ps_traning.programmers.level_0;

public class 수_조작하기_2 {
    public String solution(int[] numLog) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < numLog.length; i++) {
            int result = numLog[i] - numLog[i - 1];
            if (result == 1) sb.append("w");
            else if (result == -1) sb.append("s");
            else if (result == 10) sb.append("d");
            else if (result == -10) sb.append("a");
        }
        answer = sb.toString();
        return answer;
    }
}
