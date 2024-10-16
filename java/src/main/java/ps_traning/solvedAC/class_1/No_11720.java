package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_11720 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        String cmd = br.readLine();
        int answer = 0;
        for (char c : cmd.toCharArray()) answer += c - '0';
        System.out.println(answer);
    }
}
