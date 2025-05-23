package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1222 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine(), "+");
            int result = 0;
            while (st.hasMoreTokens()) result += Integer.valueOf(st.nextToken());
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
