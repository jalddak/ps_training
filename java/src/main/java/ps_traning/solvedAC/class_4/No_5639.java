package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class No_5639 {
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

        try {
            while (true) {
                int c = Integer.valueOf(br.readLine());
                if (c < n) {
                    tree.get(n)[1] = c;
                } else if (c > n) {
                    int maxN = n;
                    while (n != root && c > tree.get(n)[0]) {
                        n = tree.get(n)[0];
                        maxN = Math.max(maxN, n);
                    }
                    n = maxN;
                    tree.get(n)[2] = c;
                }
                tree.put(c, new int[]{n, 0, 0});
                n = c;
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
