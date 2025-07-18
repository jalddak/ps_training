package ps_traning.barkingdog.x0B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_17478 {
    private static final StringBuilder sb = new StringBuilder();
    private static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        sb.append("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.").append("\n");
        rc(0);
        System.out.print(sb);
    }

    private static void rc(int depth) {
        depthCheck(depth, "\"재귀함수가 뭔가요?\"");
        if (depth == n) {
            depthCheck(depth, "\"재귀함수는 자기 자신을 호출하는 함수라네\"");
            depthCheck(depth, "라고 답변하였지.");
            return;
        }
        depthCheck(depth, "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.");
        depthCheck(depth, "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.");
        depthCheck(depth, "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"");
        rc(depth + 1);
        depthCheck(depth, "라고 답변하였지.");
    }

    private static void depthCheck(int depth, String message) {
        for (int i = 0; i < depth; i++) sb.append("____");
        sb.append(message).append("\n");
    }
}
