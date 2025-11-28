package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_7511 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("Scenario ").append(tc).append(":").append("\n");
            int n = Integer.parseInt(br.readLine());

            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = i;

            int k = Integer.parseInt(br.readLine());
            for (int i = 0; i < k; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                arr[getParent(arr, b)] = getParent(arr, a);
            }

            int m = Integer.parseInt(br.readLine());
            for (int i = 0; i < m; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                if (getParent(arr, a) != getParent(arr, b)) sb.append(0);
                else sb.append(1);
                sb.append("\n");
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }

    private static int getParent(int[] arr, int num) {
        if (arr[num] != num) arr[num] = getParent(arr, arr[num]);
        return arr[num];
    }
}
