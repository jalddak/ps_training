package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_8958 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        for (int i = 0; i < n; i++) {
            String cmd = br.readLine();
            int score = 0;
            int plus = 1;
            for (char c : cmd.toCharArray()) {
                if (c == 'O') score += plus++;
                else plus = 1;
            }
            System.out.println(score);
        }
    }
}
