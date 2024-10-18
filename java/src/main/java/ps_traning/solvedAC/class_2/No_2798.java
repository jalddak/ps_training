package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_2798 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] cmd = new int[2];
        int index = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) cmd[index++] = Integer.valueOf(st.nextToken());

        int[] nums = new int[cmd[0]];
        index = 0;
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) nums[index++] = Integer.valueOf(st.nextToken());

        Set<Integer> set = new HashSet<>();
        boolean[] visited = new boolean[cmd[0]];
        Arrays.fill(visited, false);
        combination(0, 0, nums, visited, new int[3], 3, set);
        List<Integer> list = new ArrayList<>(List.copyOf(set));
        Collections.sort(list);
        int answer = 0;
        for (int n : list) {
            if (cmd[1] < n) break;
            answer = n;
        }
        System.out.println(answer);

    }

    public static void combination(int depth, int start, int[] arr, boolean[] visited, int[] out, int cnt, Set<Integer> result) {
        if (depth == cnt) {
            int candidate = Arrays.stream(out).sum();
            result.add(candidate);
            System.out.println(result.toString());
            return;
        }
        for (int i = start; i < arr.length; i++) {
            visited[i] = true;
            out[depth] = arr[i];
            combination(depth + 1, i + 1, arr, visited, out, cnt, result);
            visited[i] = false;
        }
    }
}
