package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_1228 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int tcCnt = 10;

        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            solution();
        }
        System.out.print(sb);

    }

    private static void solution() throws IOException {
        int n = Integer.valueOf(br.readLine());
        List<Integer> codes = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            codes.add(Integer.valueOf(st.nextToken()));
        }
        int cmdN = Integer.valueOf(br.readLine());
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            st.nextToken();
            int insertIdx = Integer.valueOf(st.nextToken());
            int cnt = Integer.valueOf(st.nextToken());
            for (int i = 0; i < cnt; i++) {
                codes.add(insertIdx + i, Integer.valueOf(st.nextToken()));
            }
        }
        for (int i = 0; i < 10; i++) {
            sb.append(codes.get(i)).append(" ");
        }
        sb.append('\n');
    }
}
