package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1074 {

    private static int n, r, c;
    private static int[] dy = {0, 0, 1, 1};
    private static int[] dx = {0, 1, 0, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int len = (int) Math.pow(2, n);
        System.out.println(calc(len, 0, 0));


    }

    private static int calc(int len, int y, int x) {
        if (len == 1) return 0;
        int half = len / 2;
        int result = 0;
        for (int d = 0; d < 4; d++) {
            int sy = y + dy[d] * half;
            int sx = x + dx[d] * half;
            if (r < sy || r >= sy + half || c < sx || c >= sx + half) continue;
            result += half * half * d + calc(half, sy, sx);
            break;
        }
        return result;
    }
}
