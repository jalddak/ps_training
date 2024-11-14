package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_11659 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        int[] nums = new int[n];
        st = new StringTokenizer(br.readLine());
        int[] ps = new int[n + 1];
        ps[0] = 0;
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.valueOf(st.nextToken());
            ps[i + 1] = ps[i] + nums[i];
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());
            sb.append(ps[e] - ps[s - 1]).append("\n");
        }
        System.out.print(sb.toString());
    }
}
