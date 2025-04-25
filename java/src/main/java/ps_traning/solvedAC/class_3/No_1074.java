package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1074 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.valueOf(st.nextToken());
        int r = Integer.valueOf(st.nextToken());
        int c = Integer.valueOf(st.nextToken());

        int length = (int) Math.pow(2, n);
        int answer = 0;
        while (length > 1) {
            int temp = length * length / 4;
            int half = length / 2;

            int d = 0;
            if (r < half && c >= half) d = 1;
            else if (r >= half && c < half) d = 2;
            else if (r >= half && c >= half) d = 3;

            answer += temp * d;

            if (r >= half) r -= half;
            if (c >= half) c -= half;
            length /= 2;
        }

        System.out.println(answer);
    }
}
