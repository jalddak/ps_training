package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class No_4012 {
    private static int n, answer;
    private static int[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            n = Integer.parseInt(br.readLine());
            board = new int[n][n];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            answer = 20000 * 8;
            Stack<Integer> stack = new Stack<>();
            stack.push(0);
            logic(stack);


            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.print(sb);
    }

    private static int synergy(List<Integer> list) {
        int result = 0;
        for (int i = 0; i < list.size(); i++) {
            for (int j = i + 1; j < list.size(); j++) {
                result += board[list.get(i)][list.get(j)] + board[list.get(j)][list.get(i)];
            }
        }
        return result;
    }

    private static void logic(Stack<Integer> stack) {
        if (stack.size() == n / 2) {
            Set<Integer> setA = new HashSet<>(stack);
            List<Integer> listA = new ArrayList<>(stack);
            List<Integer> listB = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (!setA.contains(i)) {
                    listB.add(i);
                }
            }
            answer = Math.min(answer, Math.abs(synergy(listA) - synergy(listB)));
            return;
        }

        for (int i = stack.peek() + 1; i < n; i++) {
            stack.push(i);
            logic(stack);
            stack.pop();
        }
    }
}