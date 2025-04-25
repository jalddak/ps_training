package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class No_1208 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= 10; tc++) {
            sb.append("#").append(tc).append(" ");

            int cnt = Integer.valueOf(br.readLine());
            List<Integer> heights = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 100; i++) {
                heights.add(Integer.valueOf(st.nextToken()));
            }

            for (int i = 0; i < cnt; i++) {
                int maxHeight = Collections.max(heights);
                int minHeight = Collections.min(heights);
                if (maxHeight - minHeight <= 1) break;

                int maxHeightIndex = heights.indexOf(maxHeight);
                int minHeightIndex = heights.indexOf(minHeight);
                heights.set(maxHeightIndex, heights.get(maxHeightIndex) - 1);
                heights.set(minHeightIndex, heights.get(minHeightIndex) + 1);
            }

            sb.append(Collections.max(heights) - Collections.min(heights)).append("\n");

        }

        System.out.print(sb.toString());
    }
}
