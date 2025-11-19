package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class No_14238 {

    private static int len;
    private static Map<Character, Integer> cnts = new HashMap<>();
    private static Stack<Character> stack = new Stack<>();
    private static boolean flag = false;
    private static boolean[][][][] visited = new boolean[51][51][51][3];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        len = input.length();

        cnts.put('A', 0);
        cnts.put('B', 0);
        cnts.put('C', 0);
        for (char c : input.toCharArray()) cnts.put(c, cnts.get(c) + 1);

        backTracking(-1);
        StringBuilder sb = new StringBuilder();
        if (!flag) sb.append(-1);
        else {
            for (char c : stack) {
                sb.append(c);
            }
        }
        System.out.println(sb);

    }

    private static void backTracking(int before) {
        if (before != -1 && visited[cnts.get('A')][cnts.get('B')][cnts.get('C')][before]) return;

        if (stack.size() == len) {
            flag = true;
            return;
        }

        for (char c = 'C'; c >= 'A'; c--) {
            if (cnts.get(c) > 0) {
                if (c == 'B' && (!stack.isEmpty() && stack.get(stack.size() - 1) == c)) continue;
                if (c == 'C' &&
                        ((!stack.isEmpty() && stack.get(stack.size() - 1) == c) ||
                                stack.size() >= 2 && stack.get(stack.size() - 2) == c)) continue;
                stack.push(c);
                cnts.put(c, cnts.get(c) - 1);
                backTracking(c - 'A');
                if (flag) break;
                cnts.put(c, cnts.get(c) + 1);
                stack.pop();
            }
        }

        if (before != -1)
            visited[cnts.get('A')][cnts.get('B')][cnts.get('C')][before] = true;


    }
}