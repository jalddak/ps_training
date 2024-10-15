package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_2920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> ori = new ArrayList<>();
        while (st.hasMoreTokens()) ori.add(Integer.valueOf(st.nextToken()));
        String answer = "mixed";
        int start;
        if (ori.get(0) == 1) {
            start = 0;
            for (int n : ori) {
                if (n == start + 1) start++;
                else break;
            }
            if (start == 8) answer = "ascending";
        } else if (ori.get(0) == 8) {
            start = 9;
            for (int n : ori) {
                if (n == start - 1) start--;
                else break;
            }
            if (start == 1) answer = "descending";
        }
        System.out.println(answer);
    }
}
