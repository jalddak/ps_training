package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_10989 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[] cnts = new int[10001];
        for (int i = 0; i < n; i++) {
            int num = Integer.valueOf(br.readLine());
            cnts[num] += 1;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10001; i++) {
            for (int j = 0; j < cnts[i]; j++) {
                sb.append(i);
                sb.append("\n");
            }
        }
        System.out.println(sb.toString());
    }
}
