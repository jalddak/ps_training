package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_2562 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int maxNum = 0, index = 0;
        for (int i = 0; i < 9; i++) {
            int n = Integer.valueOf(br.readLine());
            if (maxNum < n) {
                maxNum = n;
                index = i + 1;
            }
        }
        System.out.println(maxNum + "\n" + index);
    }
}
