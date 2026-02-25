package ps_traning.baekjoon.all;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_2618_orderList {

    private static int n, w;
    private static int[][] events;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        w = Integer.parseInt(br.readLine());

        events = new int[w][2];
        for (int i = 0; i < w; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            events[i][0] = Integer.parseInt(st.nextToken()) - 1;
            events[i][1] = Integer.parseInt(st.nextToken()) - 1;
        }

        Queue<Info> q = new ArrayDeque<>();
        q.add(new Info(0, 0, n - 1, n - 1, 0));

        int by = -1, bx = -1;
        for (int[] e : events) {
            int ey = e[0], ex = e[1];
            Info temp = null;
            Queue<Info> nq = new ArrayDeque<>();
            while (!q.isEmpty()) {
                Info poll = q.poll();
                Info left = new Info(poll);
                left.cost += Math.abs(left.ly - ey) + Math.abs(left.lx - ex);
                left.ly = ey;
                left.lx = ex;
                left.order.add(1);

                Info right = new Info(poll);
                right.cost += Math.abs(right.ry - ey) + Math.abs(right.rx - ex);
                right.ry = ey;
                right.rx = ex;
                right.order.add(2);


                if (poll.ry == by && poll.rx == bx) {
                    if (temp == null || temp.cost > left.cost)
                        temp = left;
                } else nq.add(left);
                if (poll.ly == by && poll.lx == bx) {
                    if (temp == null || temp.cost > right.cost)
                        temp = right;
                } else nq.add(right);
            }
            by = ey;
            bx = ex;
            if (temp != null)
                nq.add(temp);
            q = nq;
        }

        StringBuilder sb = new StringBuilder();
        int answerCost = Integer.MAX_VALUE;
        List<Integer> answerOrder = null;
        while (!q.isEmpty()) {
            Info poll = q.poll();
            if (answerCost > poll.cost) {
                answerCost = poll.cost;
                answerOrder = poll.order;
            }


        }
        sb.append(answerCost).append("\n");
        for (int o : answerOrder)
            sb.append(o).append("\n");
        System.out.println(sb);
    }

    static class Info {
        int ly, lx, ry, rx, cost;
        List<Integer> order = new ArrayList<>();

        public Info(int ly, int lx, int ry, int rx, int cost) {
            this.ly = ly;
            this.lx = lx;
            this.ry = ry;
            this.rx = rx;
            this.cost = cost;
        }

        public Info(Info before) {
            this.ly = before.ly;
            this.lx = before.lx;
            this.ry = before.ry;
            this.rx = before.rx;
            this.cost = before.cost;
            this.order.addAll(before.order);
        }

        public String toString() {
            String s = this.ly + " " + this.lx + " " + this.ry + " " + this.rx + " " + this.cost;
            return s;
        }
    }
}