package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_3307 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());

        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());
            int[] arr = new int[n];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.valueOf(st.nextToken());
            }

            List<Integer> list = new ArrayList<>();
            for (int num : arr) {
                bs(list, num);
            }

            int result = list.size();
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static void bs(List<Integer> list, int target){
        int l = -1;
        int r = list.size();

        while (l + 1 < r){
            int mid = (l + r) / 2;
            if (list.get(mid) < target){
                l = mid;
            } else if (list.get(mid) > target){
                r = mid;
            } else break;
        }

        if (r == list.size()) list.add(target);
        else list.set(r, target);
    }
}
