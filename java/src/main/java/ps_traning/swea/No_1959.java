package ps_traning.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class No_1959 {
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int m = Integer.valueOf(st.nextToken());

            int[] a = new int[n];
            int[] b = new int[m];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) a[i] = Integer.valueOf(st.nextToken());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) b[i] = Integer.valueOf(st.nextToken());

            int[] l = a.length > b.length ? a : b;
            int[] s = a.length > b.length ? b : a;

            int answer = 0;
            for (int i = 0; i < l.length - s.length + 1; i++) {
                int temp = 0;
                for (int j = 0; j < s.length; j++) {
                    temp += l[i + j] * s[j];
                }
                answer = Math.max(answer, temp);
            }
            sb.append(answer).append("\n");
        }
        System.out.print(sb);
    }
}
