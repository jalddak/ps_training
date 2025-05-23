package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class No_1223 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;
        for (int tc = 1; tc <= tcCnt; tc++) {
            Stack<Integer> numStack = new Stack<>();
            Stack<Character> buho = new Stack<>();
            int n = Integer.valueOf(br.readLine());
            char[] s = br.readLine().toCharArray();
            for (char c : s) {
                if (Character.isDigit(c)) {
                    numStack.push(c - '0');
                    continue;
                }
                if (buho.isEmpty() || (buho.peek() == '+' && c == '*')) {
                    buho.push(c);
                    continue;
                }
                calc(numStack, buho);
                buho.push(c);
            }
            while (!buho.isEmpty()) calc(numStack, buho);
            int result = numStack.pop();
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static void calc(Stack<Integer> numStack, Stack<Character> buho) {
        char before = buho.pop();
        if (before == '+') numStack.push(numStack.pop() + numStack.pop());
        else numStack.push(numStack.pop() * numStack.pop());
    }
}
