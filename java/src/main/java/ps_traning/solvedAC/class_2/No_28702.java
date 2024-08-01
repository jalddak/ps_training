package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_28702 {
    static StringBuilder sb = new StringBuilder();
    static int n = 0;
    static boolean flag = false;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception {
        for (int i = 0; i < 3; i++) {
            String temp = br.readLine();
            if (temp.chars().allMatch(Character::isDigit)) {
                flag = true;
                n = Integer.valueOf(temp) + 3 - i;
            }
        }
        if (n % 3 == 0) sb.append("Fizz");
        if (n % 5 == 0) sb.append("Buzz");
        if (sb.toString().isEmpty()) sb.append(n);
        System.out.println(sb.toString());
    }
}
