package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_1000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String[] nums = s.split(" ");
        int answer = 0;
        for (String num : nums) {
            answer += Integer.valueOf(num);
        }
        System.out.println(answer);

    }
}
