package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_15829 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long l = Long.parseLong(br.readLine());
        String str = br.readLine();
        long answer = 0;

        long temp = 1;
        for (int i = 0; i < l; i++) {
            char c = str.charAt(i);
            int n = c - 'a' + 1;
            answer += (long) (n * temp) % 1234567891;
            temp = temp * 31 % 1234567891;
        }
        answer %= 1234567891;
        System.out.println(answer);
    }
}
