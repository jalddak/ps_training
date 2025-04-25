package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class No_1206 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        for (int t = 1; t <= 10; t++) {
            int result = 0;

            int n = Integer.valueOf(br.readLine());
            int[] buildings = new int[n];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                buildings[i] = Integer.valueOf(st.nextToken());
            }

            for (int i = 2; i < n - 2; i++) {
                int[] temp = Arrays.copyOfRange(buildings, i - 2, i + 3);
                temp = Arrays.stream(temp).boxed().sorted(Comparator.reverseOrder()).mapToInt(Integer::valueOf).toArray();
                if (temp[0] == buildings[i]) result += buildings[i] - temp[1];
            }

            sb.append("#").append(t).append(" ").append(result).append("\n");
        }
        System.out.print(sb.toString());
    }
}
