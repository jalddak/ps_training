package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class No_1759 {
    private static int l, c;
    private static char[] arr;
    private static StringBuilder sb = new StringBuilder();
    private static Set<Character> m = new HashSet<>();


    public static void main(String[] args) throws IOException {
        m.add('a');
        m.add('e');
        m.add('i');
        m.add('o');
        m.add('u');

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        arr = new char[c];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < c; i++) {
            arr[i] = st.nextToken().charAt(0);
        }

        Arrays.sort(arr);

        recursion(0, 0, 0, 0, new StringBuilder());
        System.out.print(sb);

    }

    private static void recursion(int depth, int idx, int mCnt, int jCnt, StringBuilder result) {
        if (depth == l) {
            if (mCnt == 0 || jCnt < 2) return;
            sb.append(result).append("\n");
            return;
        }

        for (int i = idx; i < c; i++) {
            result.append(arr[i]);
            int nMcnt = mCnt;
            int nJcnt = jCnt;
            if (m.contains(arr[i])) nMcnt++;
            else nJcnt++;
            recursion(depth + 1, i + 1, nMcnt, nJcnt, result);
            result.setLength(result.length() - 1);
        }
    }
}
