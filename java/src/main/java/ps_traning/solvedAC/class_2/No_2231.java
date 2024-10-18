package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_2231 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String strNum = br.readLine();
        int num = Integer.parseInt(strNum);
        int len = strNum.length();
        boolean flag = false;
        for (int n = num - (len * 9); n < num; n++) {
            if (n < 0) continue;
            int candidate = n + Arrays.stream(String.valueOf(n).split(""))
                    .mapToInt(Integer::valueOf).sum();
            if (candidate == num) {
                System.out.println(n);
                flag = true;
                break;
            }
        }
        if (!flag) System.out.println(0);
    }
}
