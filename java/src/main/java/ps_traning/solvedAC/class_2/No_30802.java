package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_30802 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.valueOf(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> ts = new ArrayList<>();
        while (st.hasMoreTokens()) {
            ts.add(Integer.valueOf(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        int t = Integer.valueOf(st.nextToken());
        int p = Integer.valueOf(st.nextToken());

        int answer = 0;
        for (int i = 0; i < ts.size(); i++) {
            answer += ts.get(i) / t;
            if (ts.get(i) % t > 0) answer += 1;
        }
        System.out.println(answer);
        System.out.println((N / p) + " " + (N % p));
    }
}
