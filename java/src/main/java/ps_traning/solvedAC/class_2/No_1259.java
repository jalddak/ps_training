package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_1259 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String str = br.readLine();
            int len = str.length();
            if (str.equals("0")) return;
            boolean flag = true;
            for (int i = 0; i < len / 2; i++) {
                if (str.charAt(i) != str.charAt(len - 1 - i)) {
                    flag = false;
                    break;
                }
            }
            if (flag) System.out.println("yes");
            else System.out.println("no");

        }

    }
}
