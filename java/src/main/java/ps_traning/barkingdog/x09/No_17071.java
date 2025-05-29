package ps_traning.barkingdog.x09;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_17071 {
    private static int max = 500001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.valueOf(st.nextToken());
        int k = Integer.valueOf(st.nextToken());

        int[][] visited = new int[max][2];
        for (int i = 0; i < max; i++) {
            visited[i] = new int[]{max, max};
        }

        int result = -1;
        visited[n][0] = 0;
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{n, 0});
        int time = 0;
        while (k < max) {
            if (visited[k][time % 2] <= time) {
                result = time;
                break;
            }
            time++;
            k += time;

            Stack<int[]> next = new Stack<>();
            while (!stack.isEmpty()) {
                int[] pop = stack.pop();
                int x = pop[0], t = pop[1];
                int nt = t + 1;
                if (x - 1 >= 0 && visited[x - 1][nt % 2] > nt) {
                    visited[x - 1][nt % 2] = nt;
                    next.push(new int[]{x - 1, nt});
                }
                if (x + 1 < max && visited[x + 1][nt % 2] > nt) {
                    visited[x + 1][nt % 2] = nt;
                    next.push(new int[]{x + 1, nt});
                }
                if (x * 2 < max && visited[x * 2][nt % 2] > nt) {
                    visited[x * 2][nt % 2] = nt;
                    next.push(new int[]{x * 2, nt});
                }
            }
            stack = next;
        }
        System.out.println(result);
    }
}
