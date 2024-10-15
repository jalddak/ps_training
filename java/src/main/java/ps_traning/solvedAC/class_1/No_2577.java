package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_2577 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = 1;
        for (int i = 0; i < 3; i++) n *= Integer.valueOf(br.readLine());
        String sn = String.valueOf(n);
        int[] flag = new int[10];
        for (char c : sn.toCharArray()) flag[c - '0'] += 1;
        for (int num : flag) System.out.println(num);
    }
}
