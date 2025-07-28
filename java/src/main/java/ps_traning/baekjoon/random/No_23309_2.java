package ps_traning.baekjoon.random;

import java.io.*;
import java.util.StringTokenizer;

/**
 * 시간초과
 * <p>
 * BufferedWriter 사용
 * Node 이용해서 연결리스트 사용
 */
public class No_23309_2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Node[] nodes = new Node[1000001];

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
                    bw.write(temp.num + "\n");
                    cur.next = newNode;
                    newNode.prev = cur;
                    newNode.next = temp;
                    temp.prev = newNode;
                } else {
                    Node temp = cur.prev;
                    bw.write(temp.num + "\n");
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
                    bw.write(temp.num + "\n");
                    cur.next = temp.next;
                    cur.next.prev = cur;
                } else {
                    Node temp = cur.prev;
                    bw.write(temp.num + "\n");
                    cur.prev = temp.prev;
                    cur.prev.next = cur;
                }
            }
        }
        bw.flush();
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