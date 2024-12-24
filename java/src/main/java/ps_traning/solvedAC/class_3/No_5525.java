package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_5525 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int m = Integer.valueOf(br.readLine());
        char[] input = br.readLine().toCharArray();

        char check = 'O';
        int cnt = 0;
        int answer = 0;
        for (char c : input) {
            if (c == 'I') {
                if (check == 'I') cnt = 0;
                if (cnt >= n) answer += 1;
                check = 'I';
            } else if (c == 'O') {
                if (check == 'O') cnt = 0;
                else cnt += 1;
                check = 'O';
            }
        }
        System.out.println(answer);
    }
}
