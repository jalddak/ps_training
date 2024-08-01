package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_31430 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.valueOf(br.readLine());
        int b = Integer.valueOf(br.readLine());
        int c = Integer.valueOf(br.readLine());
        System.out.println(a + b - c);
        StringBuilder sb = new StringBuilder();
        sb.append(a);
        sb.append(b);
        int temp = Integer.valueOf(sb.toString());
        System.out.println(temp - c);
    }

}
