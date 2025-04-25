package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_2166 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<long[]> xys = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long[] temp = {Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken())};
            xys.add(temp);
        }
        xys.add(xys.get(0));

        long plus = 0, minus = 0;
        for (int i = 0; i < n; i++) {
            plus += xys.get(i)[0] * xys.get(i + 1)[1];
            minus += xys.get(i)[1] * xys.get(i + 1)[0];
        }

        double result = Math.abs(plus - minus) / 2.0;
        System.out.printf("%.1f", result);
    }
}
