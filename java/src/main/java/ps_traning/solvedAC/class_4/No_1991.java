package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1991 {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static StringBuilder sb;
    private static int n;
    private static Map<Character, char[]> edges;
    private static List<Character>[] result;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        edges = new HashMap<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            edges.put(st.nextToken().charAt(0), new char[]{st.nextToken().charAt(0), st.nextToken().charAt(0)});
        }

        result = new ArrayList[3];
        for (int i = 0; i < 3; i++) {
            result[i] = new ArrayList<>();
        }
        solution('A');
        sb = new StringBuilder();

        for (int i = 0; i < 3; i++) {
            for (char c : result[i]) sb.append(c);
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }

    private static void solution(char node) {
        result[0].add(node);
        for (int i = 0; i < 2; i++) {
            if (i == 1) result[1].add(node);
            if (edges.get(node)[i] == '.') continue;
            solution(edges.get(node)[i]);
        }
        result[2].add(node);
    }
}
