package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 세그먼트 트리
 */
public class No_1306 {
    private static int n, m;
    private static int[] lights;
    private static int[][] segTree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());

        lights = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            lights[i] = Integer.valueOf(st.nextToken());
        }

        // segTree : [num, first, last]
        segTree = new int[4 * n + 1][3];
        makeSegTree(1, 0, n - 1);

        int range = 2 * m - 1;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n - range + 1; i++) {
            int first = i;
            int last = first + range - 1;
            sb.append(searchMax(1, first, last)).append(" ");
        }
        sb.append("\n");
        System.out.print(sb);
    }

    private static int searchMax(int idx, int first, int last) {
        int left = segTree[idx][1];
        int right = segTree[idx][2];

        if (left >= first && right <= last) return segTree[idx][0];
        int mid = (left + right) / 2;

        int[] candidates = {-1, -1};
        if (first <= mid) candidates[0] = searchMax(idx * 2, first, last);
        if (last > mid) candidates[1] = searchMax(idx * 2 + 1, first, last);

        return Arrays.stream(candidates).max().getAsInt();
    }

    private static void makeSegTree(int idx, int first, int last) {
        if (first == last) {
            segTree[idx] = new int[]{lights[first], first, last};
            return;
        }

        int mid = (first + last) / 2;
        makeSegTree(idx * 2, first, mid);
        makeSegTree(idx * 2 + 1, mid + 1, last);
        segTree[idx] = new int[]{Math.max(segTree[idx * 2][0], segTree[idx * 2 + 1][0]), first, last};
    }
}
