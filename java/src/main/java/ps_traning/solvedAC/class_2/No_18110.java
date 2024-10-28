package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_18110 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        if (n == 0) {
            System.out.println(0);
            System.exit(0);
        }
        int[] scores = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = Integer.valueOf(br.readLine());
        }
        int len = scores.length;
        int e = (int) (len * 0.15 + 0.5);
        Arrays.sort(scores);
        int[] temp = Arrays.copyOfRange(scores, e, len - e);
        System.out.println((int) ((double) Arrays.stream(temp).sum() / (len - 2 * e) + 0.5));
    }
}
