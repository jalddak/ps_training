package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class No_1920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        Set<Integer> s = new HashSet<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) s.add(Integer.valueOf(st.nextToken()));
        int m = Integer.valueOf(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            if (s.contains(num)) sb.append("1\n");
            else sb.append("0\n");
        }
        System.out.print(sb.toString());
    }
}
