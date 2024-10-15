package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_2753 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        if (n % 400 == 0 || (n % 4 == 0 && n % 100 != 0)) {
            System.out.println(1);
        } else System.out.println(0);
    }
}
