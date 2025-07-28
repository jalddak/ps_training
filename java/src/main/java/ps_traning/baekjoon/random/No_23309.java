package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * StringBuilder 사용
 * Node 만들어서 연결리스트 사용
 */
public class No_23309 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Node[] nodes = new Node[1000001];

        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());
        Node tail = null;
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            Node node = new Node(num);
            if (tail == null) {
                tail = node;
                tail.next = node;
                tail.prev = node;
            } else {
                Node temp = tail.next;
                tail.next = node;
                node.prev = tail;
                node.next = temp;
                temp.prev = node;
                tail = node;
            }
            nodes[num] = node;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.charAt(0) == 'B') {
                int n1 = Integer.parseInt(st.nextToken());
                int n2 = Integer.parseInt(st.nextToken());
                Node cur = nodes[n1];
                Node newNode = new Node(n2);
                nodes[n2] = newNode;
                if (cmd.charAt(1) == 'N') {
                    Node temp = cur.next;
                    sb.append(temp.num).append("\n");
                    cur.next = newNode;
                    newNode.prev = cur;
                    newNode.next = temp;
                    temp.prev = newNode;
                } else {
                    Node temp = cur.prev;
                    sb.append(temp.num).append("\n");
                    cur.prev = newNode;
                    newNode.next = cur;
                    newNode.prev = temp;
                    temp.next = newNode;
                }
            } else {
                int num = Integer.parseInt(st.nextToken());
                Node cur = nodes[num];
                if (cmd.charAt(1) == 'N') {
                    Node temp = cur.next;
                    sb.append(temp.num).append("\n");
                    cur.next = temp.next;
                    cur.next.prev = cur;
                } else {
                    Node temp = cur.prev;
                    sb.append(temp.num).append("\n");
                    cur.prev = temp.prev;
                    cur.prev.next = cur;
                }
            }
        }
        System.out.print(sb);
    }

    private static class Node {
        private final int num;
        private Node prev, next;

        public Node(int num) {
            this.num = num;
            this.prev = null;
            this.next = null;
        }
    }
}