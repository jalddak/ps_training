package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_7568 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[][] arr = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int index = 0;
            while (st.hasMoreTokens()) arr[i][index++] = Integer.valueOf(st.nextToken());
        }

        int[] answer = new int[n];
        Arrays.fill(answer, 1);
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i][0] > arr[j][0] && arr[i][1] > arr[j][1]) answer[j] += 1;
                else if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) answer[i] += 1;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int a : answer) {
            sb.append(a + "\n");
        }
        System.out.println(sb.toString());
    }
}
