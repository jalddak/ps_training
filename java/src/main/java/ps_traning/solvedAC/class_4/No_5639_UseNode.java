package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_5639_UseNode {
    private static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        Node root = new Node(n);
        sb = new StringBuilder();

        try {
            while (true) {
                int c = Integer.valueOf(br.readLine());
                root.insert(c);
            }

        } catch (Exception e) {
            postOrder(root);
            System.out.print(sb.toString());
        }
    }

    private static void postOrder(Node node) {
        if (node == null) return;
        postOrder(node.left);
        postOrder(node.right);
        sb.append(node.value).append("\n");
    }

    public static class Node {
        int value;
        Node left, right;

        public Node(int value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }

        public void insert(int value) {
            if (value < this.value) {
                if (this.left == null) this.left = new Node(value);
                else this.left.insert(value);
            } else if (value > this.value) {
                if (this.right == null) this.right = new Node(value);
                else this.right.insert(value);
            }
        }
    }
}
