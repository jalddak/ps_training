package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_16987 {

    private static int n, answer;
    private static int[][] eggInfo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        eggInfo = new int[n][2];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            eggInfo[i][0] = Integer.valueOf(st.nextToken());
            eggInfo[i][1] = Integer.valueOf(st.nextToken());

        }

        recursion(0, 0);
        System.out.println(answer);
    }

    private static void recursion(int depth, int cnt) {

        if (depth == n) {
            answer = Math.max(answer, cnt);
            return;
        }

        boolean flag = true;
        for (int i = 0; i < n; i++) {
            if (eggInfo[depth][0] <= 0) {
                recursion(depth + 1, cnt);
                continue;
            }

            if (depth == i || eggInfo[i][0] <= 0) continue;

            flag = false;
            eggInfo[depth][0] -= eggInfo[i][1];
            eggInfo[i][0] -= eggInfo[depth][1];
            cnt += eggInfo[depth][0] <= 0 ? 1 : 0;
            cnt += eggInfo[i][0] <= 0 ? 1 : 0;
            recursion(depth + 1, cnt);
            cnt -= eggInfo[depth][0] <= 0 && eggInfo[depth][0] + eggInfo[i][1] > 0 ? 1 : 0;
            cnt -= eggInfo[i][0] <= 0 && eggInfo[i][0] + eggInfo[depth][1] > 0 ? 1 : 0;
            eggInfo[depth][0] += eggInfo[i][1];
            eggInfo[i][0] += eggInfo[depth][1];

        }

        if (flag) recursion(depth + 1, cnt);
    }
}
