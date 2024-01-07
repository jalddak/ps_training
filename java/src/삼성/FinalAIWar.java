package 삼성;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class FinalAIWar {

    private static final List<int[]> candidates = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();

        List<Integer> results = new ArrayList<>();
        for (int test_case = 1; test_case <= T; test_case++) {
            candidates.clear();
            int N = sc.nextInt();
            sc.nextLine();
            int[] nums = new int[N];
            boolean[] visited = new boolean[N];
            for (int i = 0; i < N; i++) {
                nums[i] = i;
                visited[i] = false;
            }
            permutation(nums, new int[3], visited, 0, N, 3);

            int sumLoses = 0;
            int[][] loses = new int[N][];
            for (int i = 0; i < N; i++) {
                int[] ability = Stream.of(sc.nextLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
                int sumAbility = Arrays.stream(ability).sum();
                int[] lose = new int[3];
                for (int j = 0; j < 3; j++) {
                    lose[j] = sumAbility - ability[j];
                }
                sumLoses += Arrays.stream(lose).min().getAsInt();
                loses[i] = lose;
            }

            if (N < 3) {
                results.add(-1);
                continue;
            }

            int result = 2 * N * (int) Math.pow(10, 6) + 1;
            for (int[] candidate : candidates) {
                int temp = sumLoses - Arrays.stream(loses[candidate[0]]).min().getAsInt()
                        - Arrays.stream(loses[candidate[1]]).min().getAsInt()
                        - Arrays.stream(loses[candidate[2]]).min().getAsInt();
                temp += loses[candidate[0]][0] + loses[candidate[1]][1] + loses[candidate[2]][2];

                if (result > temp) {
                    result = temp;
                }
            }
            results.add(result);
        }
        int order = 1;
        for (Integer result : results) {
            System.out.printf("#%d %d%n", order, result);
            order++;
        }
    }

    public static void permutation(int[] arr, int[] candidate, boolean[] visited, int depth, int n, int r) {
        if (depth == r) {
            candidates.add(candidate.clone());
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                candidate[depth] = arr[i];
                permutation(arr, candidate, visited, depth + 1, n, r);
                visited[i] = false;
            }
        }
    }


}
