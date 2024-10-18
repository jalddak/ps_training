package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_30802_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[] sizes = new int[6];
        int index = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) sizes[index++] = Integer.valueOf(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] tp = new int[2];
        index = 0;
        while (st.hasMoreTokens()) tp[index++] = Integer.valueOf(st.nextToken());

        int a1 = 0;
        for (int s : sizes) a1 += s / tp[0] + ((s % tp[0] > 0) ? 1 : 0);
        System.out.println(a1);
        System.out.println(n / tp[1] + " " + n % tp[1]);
    }
}
