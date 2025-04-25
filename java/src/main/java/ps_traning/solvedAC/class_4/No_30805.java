package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_30805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        List<Integer> a = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a.add(Integer.valueOf(st.nextToken()));
        }
        int m = Integer.valueOf(br.readLine());
        List<Integer> b = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            b.add(Integer.valueOf(st.nextToken()));
        }

        List<Integer> result = new ArrayList<>();

        Set<Integer> setA = new HashSet<>(a);
        Set<Integer> setB = new HashSet<>(b);
        setA.retainAll(setB);
        while (!setA.isEmpty()) {
            int maxN = setA.stream().mapToInt(Integer::valueOf).max().getAsInt();
            result.add(maxN);
            a = a.subList(a.indexOf(maxN) + 1, a.size());
            b = b.subList(b.indexOf(maxN) + 1, b.size());
            setA = new HashSet<>(a);
            setB = new HashSet<>(b);
            setA.retainAll(setB);

        }

        StringBuilder sb = new StringBuilder();
        sb.append(result.size()).append("\n");
        for (int num : result) {
            sb.append(num).append(" ");
        }
        System.out.println(sb.toString());
    }
}
