package ps_traning.algostudy._250826.programmers;

import java.util.Arrays;

class No_389480 {
    public int solution(int[][] info, int n, int m) {

        Arrays.sort(info, (a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return -((a[0] - a[1]) - (b[0] - b[1]));
        });

        int a = 0;
        int b = 0;

        for (int[] i : info) {
            if (b + i[1] < m) b += i[1];
            else if (a + i[0] < n) a += i[0];
            else {
                a = -1;
                break;
            }
        }

        return a;
    }
}
