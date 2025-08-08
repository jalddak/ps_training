package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_14626 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        int x = 1;
        int sum = 0;
        int need = -1;
        int idx = 0;
        for (char n : s.toCharArray()) {
            if (idx == 12) break;
            if (n != '*') sum += (n - '0') * x;
            else need = x;
            x = x == 1 ? 3 : 1;
            idx++;
        }

        int answer = -1;
        for (int i = 0; i <= 9; i++) {
            if ((s.charAt(12) - '0' == 0 && (sum + (need * i)) % 10 == 0)
                    || (10 - (sum + (need * i)) % 10 == s.charAt(12) - '0')) {
                answer = i;
                break;
            }
        }

        System.out.println(answer);
    }
}
