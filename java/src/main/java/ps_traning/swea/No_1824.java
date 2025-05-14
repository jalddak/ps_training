package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1824 {
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};
    private static Map<Character, Integer> map = new HashMap<>();
    private static Set<Integer> nums = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        map.put('^', 0);
        map.put('>', 1);
        map.put('v', 2);
        map.put('<', 3);
        for (int i = 0; i < 10; i++) {
            nums.add(i);
        }

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");

            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.valueOf(st.nextToken());
            int c = Integer.valueOf(st.nextToken());
            char[][] board = new char[r][c];
            for (int i = 0; i < r; i++) {
                board[i] = br.readLine().toCharArray();
            }

            int memory = 0;
            boolean[][][][] visited = new boolean[r][c][4][16];

            Stack<int[]> stack = new Stack<>();
            stack.push(new int[]{0, 0, 1});
            visited[0][0][1][memory] = true;

            String result = "NO";
            while (!stack.isEmpty()) {
                int[] pop = stack.pop();
                int y = pop[0], x = pop[1], d = pop[2];
                if (map.containsKey(board[y][x])) {
                    d = map.get(board[y][x]);
                    checkNext(r, c, y, x, d, memory, stack, visited);
                } else if (board[y][x] == '_') {
                    if (memory == 0) d = 1;
                    else d = 3;
                    checkNext(r, c, y, x, d, memory, stack, visited);
                } else if (board[y][x] == '|') {
                    if (memory == 0) d = 2;
                    else d = 0;
                    checkNext(r, c, y, x, d, memory, stack, visited);
                } else if (board[y][x] == '?') {
                    for (d = 0; d < 4; d++) {
                        checkNext(r, c, y, x, d, memory, stack, visited);
                    }
                } else if (board[y][x] == '.') {
                    checkNext(r, c, y, x, d, memory, stack, visited);
                } else if (board[y][x] == '@') {
                    result = "YES";
                    break;
                } else if (nums.contains(board[y][x] - '0')) {
                    memory = board[y][x] - '0';
                    checkNext(r, c, y, x, d, memory, stack, visited);
                } else if (board[y][x] == '+') {
                    memory++;
                    if (memory == 16) memory = 0;
                    checkNext(r, c, y, x, d, memory, stack, visited);
                } else if (board[y][x] == '-') {
                    memory--;
                    if (memory == -1) memory = 15;
                    checkNext(r, c, y, x, d, memory, stack, visited);
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static void checkNext(int r, int c, int y, int x, int d, int memory, Stack<int[]> stack, boolean[][][][] visited) {
        int ny = y + dy[d];
        int nx = x + dx[d];
        if (ny >= r) ny = 0;
        if (nx >= c) nx = 0;
        if (ny < 0) ny = r - 1;
        if (nx < 0) nx = c - 1;
        if (visited[ny][nx][d][memory]) return;
        visited[ny][nx][d][memory] = true;
        stack.push(new int[]{ny, nx, d});
    }
}
