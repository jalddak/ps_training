package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2869 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] abv = new int[3];
        int index = 0;
        while (st.hasMoreTokens()) abv[index++] = Integer.valueOf(st.nextToken());
        int h = abv[2] - abv[1];
        int r = abv[0] - abv[1];
        int answer = (h / r) + (h % r > 0 ? 1 : 0);
        System.out.println(answer);

    }
}
