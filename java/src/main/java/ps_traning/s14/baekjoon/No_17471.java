package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_17471 {

    private static int n, result, sum;
    private static int[] cnts;
    private static List<Integer>[] edges;
    private static Set<Integer> set;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        cnts = new int[n + 1];
        set = new HashSet<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            cnts[i] = Integer.parseInt(st.nextToken());
            sum += cnts[i];
            set.add(i);
        }
        result = sum;

        edges = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            edges[i] = new ArrayList<>();
            int cnt = Integer.parseInt(st.nextToken());
            for (int j = 0; j < cnt; j++) {
                edges[i].add(Integer.parseInt(st.nextToken()));
            }
        }

        recursion(0, new HashSet<>(), 0, 1);
        System.out.println(result != sum ? result : -1);

    }

    private static void recursion(int depth, Set<Integer> visited, int preSum, int node) {

        if (depth == n / 2) return;

        for (int i = node; i <= n; i++) {
            if (visited.contains(i)) continue;
            visited.add(i);
            set.remove(i);

            int another = 0;
            for (int temp : set) {
                another = temp;
                break;
            }

            int tempA = (check(i, visited, new boolean[n + 1]));
            int tempB = (check(another, set, new boolean[n + 1]));
            int nPreSum = preSum + cnts[i];
            if (tempA + tempB == n) {
                result = Math.min(result, Math.abs((sum - nPreSum) - nPreSum));
            }
            recursion(depth + 1, visited, nPreSum, i + 1);

            set.add(i);
            visited.remove(i);
        }
    }

    private static int check(int node, Set<Integer> checked, boolean[] visited) {
        visited[node] = true;
        int result = 1;
        if (edges[node].isEmpty()) return result;

        for (int next : edges[node]) {
            if (!checked.contains(next) || visited[next]) continue;
            result += check(next, checked, visited);
        }
        return result;
    }
}
