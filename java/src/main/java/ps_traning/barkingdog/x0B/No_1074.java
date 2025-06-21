package ps_traning.barkingdog.x0B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1074 {
    private static int[][] w = {{0, 1}, {2, 3}};
    private static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.valueOf(st.nextToken());
        int r = Integer.valueOf(st.nextToken());
        int c = Integer.valueOf(st.nextToken());
        rc(n, r, c);
        System.out.println(answer);
    }

    private static void rc(int n, int r, int c) {
        if (n == 0) return;
        int temp = 1 << (n - 1);
        answer += temp * temp * w[r / temp][c / temp];
        rc(n - 1, r % temp, c % temp);
    }
}
