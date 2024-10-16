package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_31403 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.valueOf(br.readLine());
        int b = Integer.valueOf(br.readLine());
        int c = Integer.valueOf(br.readLine());
        System.out.println(a + b - c);
        System.out.println(Integer.valueOf("" + a + b) - c);
    }
}
