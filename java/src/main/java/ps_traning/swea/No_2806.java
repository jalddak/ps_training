package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_2806 {
    private static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int tcCnt = Integer.valueOf(br.readLine());

        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            result = 0;
            int n = Integer.valueOf(br.readLine());
            int[] info = new int[n];
            Arrays.fill(info, -1);
            dfs(0, n, info);
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static void dfs(int depth, int n, int[] info) {
        if (depth == n) {
            result++;
            return;
        }

        for (int i = 0; i < n; i++) {
            boolean check = true;
            for (int j = 0; j < depth; j++) {
                if (info[j] == i || Math.abs(j - depth) == Math.abs(info[j] - i)) {
                    check = false;
                    break;
                }
            }
            if (!check) continue;
            info[depth] = i;
            dfs(depth + 1, n, info);
        }
    }
}
