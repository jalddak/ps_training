package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 세그먼트 트리 (개선)
 */
public class No_1306_2 {
    private static int n, m;
    private static int[] lights, segTree;

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
        segTree = new int[4 * n];
        makeSegTree(1, 0, n - 1);

        int range = 2 * m - 1;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n - range + 1; i++) {
            int left = i;
            int right = left + range - 1;
            sb.append(searchMax(1, 0, n - 1, left, right)).append(" ");
        }
        sb.append("\n");
        System.out.print(sb);
    }

    private static int searchMax(int idx, int first, int last, int left, int right) {

        if (first >= left && last <= right) return segTree[idx];
        int mid = (first + last) / 2;

        int leftMax = -1;
        int rightMax = -1;
        if (left <= mid) leftMax = searchMax(idx * 2, first, mid, left, right);
        if (right > mid) rightMax = searchMax(idx * 2 + 1, mid + 1, last, left, right);

        return Math.max(leftMax, rightMax);
    }

    private static void makeSegTree(int idx, int first, int last) {
        if (first == last) {
            segTree[idx] = lights[first];
            return;
        }

        int mid = (first + last) / 2;
        makeSegTree(idx * 2, first, mid);
        makeSegTree(idx * 2 + 1, mid + 1, last);
        segTree[idx] = Math.max(segTree[idx * 2], segTree[idx * 2 + 1]);
    }
}
