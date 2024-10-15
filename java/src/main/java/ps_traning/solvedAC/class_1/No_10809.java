package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_10809 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int[] apb = new int[26];
        for (int i = 0; i < apb.length; i++) {
            apb[i] = -1;
        }
        int n = 0;
        for (char c : s.toCharArray()) {
            int index = (int) c - 97;
            if (apb[index] == -1) apb[index] = n;
            n++;
        }
        for (int num : apb) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
