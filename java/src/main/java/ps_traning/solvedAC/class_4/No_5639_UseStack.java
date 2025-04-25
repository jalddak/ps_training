package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class No_5639_UseStack {
    private static StringBuilder sb;
    private static int root;
    private static Map<Integer, int[]> tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        root = n;
        tree = new HashMap<>();
        tree.put(root, new int[]{0, 0, 0});
        sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        stack.push(root);

        try {
            while (true) {
                int c = Integer.valueOf(br.readLine());
                n = stack.peek();
                if (c < n) {
                    tree.get(n)[1] = c;
                } else if (c > n) {
                    while (!stack.isEmpty() && c > stack.peek()) {
                        n = stack.pop();
                    }
                    tree.get(n)[2] = c;
                }
                tree.put(c, new int[]{n, 0, 0});
                stack.push(c);
            }

        } catch (Exception e) {
            postOrder(root);
            System.out.print(sb.toString());
        }
    }

    private static void postOrder(int node) {
        for (int i = 1; i <= 2; i++) {
            int child = tree.get(node)[i];
            if (child == 0) continue;
            postOrder(child);
        }
        sb.append(node).append("\n");
    }
}
