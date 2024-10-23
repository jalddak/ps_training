package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_1436 {
    public static void main(String[] args) throws IOException {
        int n = Integer.valueOf(new BufferedReader(new InputStreamReader(System.in)).readLine());
        int num = 0;
        int cnt = 0;
        while (cnt < n) {
            num++;
            if (String.valueOf(num).contains("666")) cnt++;
        }
        System.out.println(num);
    }
}
