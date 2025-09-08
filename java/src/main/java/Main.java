import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int n, t;
    private static String[][] board;
    private static int[][] believe;
    private static int[] dy = {-1, 1, 0, 0};
    private static int[] dx = {0, 0, -1, 1};
    private static PriorityQueue<int[]> pq;

    public static void main(String[] args) throws Exception {
        // Please write your code here.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        board = new String[n][n];

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = String.valueOf(input.charAt(j));
            }
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                believe[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        pq = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) {
                int bP = believe[b[1]][b[2]] - believe[a[1]][a[2]];
                if (bP == 0) {
                    if (a[1] == b[1]) return a[2] - b[2];
                    return a[1] - b[1];
                }
                return bP;
            }
            return a[0] - b[0];
        });

    }

    private static void lunch() {
        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]) continue;
                visited[i][j] = true;
                Queue<int[]> q = new ArrayDeque<>();
                int ry = i, rx = j;
                while (!q.isEmpty()) {
                    int[] poll = q.poll();
                    int y = poll[0], x = poll[1];
                    if (believe[y][x] > believe[ry][rx]
                            || (believe[y][x] == believe[ry][rx] && (y < ry || (y == ry && x < rx)))) {
                        ry = y;
                        rx = x;
                    }

                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny >= n || nx >= n || ny < 0 || nx < 0 || !board[ny][nx].equals(board[y][x]) || visited[ny][nx])
                            continue;
                        visited[ny][nx] = true;
                        q.add(new int[]{ny, nx});
                    }
                }
                pq.offer(new int[]{board[ry][rx].length(), ry, rx});
            }
        }
    }

    private static void morning() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                believe[i][j] += 1;
            }
        }
    }
}