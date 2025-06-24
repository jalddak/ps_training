package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_15649_try_improve {
    private static final StringBuilder sb = new StringBuilder();
    private static int n, m;
    private static int[] result;
    private static boolean[] check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        result = new int[n + 1];
        check = new boolean[n + 1];

        back(0);
        System.out.print(sb);

    }

    private static void back(int depth) {
        if (depth == m) {
            for (int i = 0; i < m; i++)
                sb.append(result[i]).append(" ");
            sb.append("\n");
            return;
        }

        for (int i = 1; i <= n; i++) {
            if (check[i]) continue;
            result[depth] = i;
            check[i] = true;
            back(depth + 1);
            check[i] = false;
        }
    }
}
