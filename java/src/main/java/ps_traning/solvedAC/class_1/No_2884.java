package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2884 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] hm = new int[2];
        int index = 0;
        while (st.hasMoreTokens()) hm[index++] = Integer.valueOf(st.nextToken());
        int h = hm[0], m = hm[1];
        m -= 45;
        if (m < 0) {
            h -= 1;
            m += 60;
        }
        if (h < 0) h += 24;
        System.out.println(h + " " + m);
    }
}
