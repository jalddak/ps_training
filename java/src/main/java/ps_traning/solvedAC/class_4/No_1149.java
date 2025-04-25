package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class No_1149 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        List<int[]> dp = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        dp.add(new int[]{Integer.valueOf(st.nextToken())
                , Integer.valueOf(st.nextToken())
                , Integer.valueOf(st.nextToken())});

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            dp.add(new int[]{Integer.valueOf(st.nextToken()) + Math.min(dp.get(i)[1], dp.get(i)[2])
                    , Integer.valueOf(st.nextToken()) + Math.min(dp.get(i)[0], dp.get(i)[2])
                    , Integer.valueOf(st.nextToken()) + Math.min(dp.get(i)[0], dp.get(i)[1])});

        }
        System.out.println(Arrays.stream(dp.get(n - 1)).min().getAsInt());
    }
}
