package ps_traning.algostudy._250925.programmers;

import java.util.Stack;

class No_150369 {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;

        Stack<int[]> ds = new Stack<>();
        Stack<int[]> ps = new Stack<>();

        for (int i = 0; i < n; i++) {
            if (deliveries[i] != 0) ds.push(new int[]{i + 1, deliveries[i]});
            if (pickups[i] != 0) ps.push(new int[]{i + 1, pickups[i]});
        }

        while (!ds.isEmpty() || !ps.isEmpty()) {
            int dn = ds.isEmpty() ? 0 : ds.peek()[0];
            int pn = ps.isEmpty() ? 0 : ps.peek()[0];
            answer += 2 * Math.max(dn, pn);
            logic(cap, ds);
            logic(cap, ps);
        }
        return answer;
    }

    public void logic(int cap, Stack<int[]> s) {
        while (cap > 0 && !s.isEmpty()) {
            if (cap >= s.peek()[1]) cap -= s.pop()[1];
            else {
                s.peek()[1] -= cap;
                cap = 0;
            }
        }
    }
}