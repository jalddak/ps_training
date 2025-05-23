package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_2817 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int k = Integer.valueOf(st.nextToken());
            int[] arr = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.valueOf(st.nextToken());
            }
            Arrays.sort(arr);


            int result = recursion(arr, 0, 0, n, k);
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static int recursion(int[] arr, int cur, int index, int n, int k) {
        int result = 0;
        for (int i = index; i < n; i++) {
            int next = cur + arr[i];
            if (next > k) break;
            if (next == k) {
                result++;
                continue;
            }
            result += recursion(arr, next, i + 1, n, k);
        }
        return result;
    }
}
