package ps_traning.algostudy._250819.programmers;

import java.util.Arrays;

class No_42884 {

    public static void main(String[] args) {
        No_42884 sol = new No_42884();
        sol.solution(new int[][]{{-20, -15}, {-14, -5}, {-18, -13}, {-5, -3}});
    }

    public int solution(int[][] routes) {
        int answer = 1;

        Arrays.sort(routes, (a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return a[0] - b[0];
        });

        int l = routes[0][0];
        int r = routes[0][1];
        for (int i = 1; i < routes.length; i++) {
            if (routes[i][0] > r) {
                answer += 1;
                l = routes[i][0];
                r = routes[i][1];
                continue;
            }
            l = Math.max(l, routes[i][0]);
            r = Math.min(r, routes[i][1]);
        }

        return answer;
    }
}
