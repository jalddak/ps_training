package ps_traning.codetree.samsung;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 해설 읽고 나서 최적화 진행.
 * 1. 우선 print 메서드 삭제
 * 2. 아침에 신앙심 1 더하고 점심에 1 뺴주는 로직 삭제.
 * 3. 비트마스킹으로 보드 변경 따라서 combine 메서드도 삭제.
 */
public class Y25_H1_AM_NO_1_Opt {

    private static int n, t;
    private static int[][] board;
    private static int[][] believe;
    private static int[] dr = {-1, 1, 0, 0};
    private static int[] dc = {0, 0, -1, 1};
    private static PriorityQueue<int[]> pq;

    public static void main(String[] args) throws Exception {
        // Please write your code here.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        board = new int[n][n];
        believe = new int[n][n];

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < n; j++) {
                int num = 1;
                if (input.charAt(j) == 'C') num <<= 1;
                else if (input.charAt(j) == 'M') num <<= 2;
                board[i][j] = num;
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

        int[] order = {7, 3, 5, 6, 4, 2, 1};
        int[] result;

        StringBuilder sb = new StringBuilder();
        for (int tc = 0; tc < t; tc++) {
            result = new int[7];
            lunch();
            dinner();


            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < 7; k++) {
                        if (order[k] == board[i][j]) result[k] += believe[i][j];
                    }
                }
            }
            for (int i = 0; i < 7; i++) {
                sb.append(result[i]).append(" ");
            }
            sb.append("\n");
        }

        System.out.print(sb);

    }

    private static void dinner() {

        boolean[][] protect = new boolean[n][n];

        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int len = poll[0], r = poll[1], c = poll[2];
            if (protect[r][c]) continue;
            int b = believe[r][c];
            int d = b % 4;
            int x = b - 1;
            believe[r][c] = 1;

            int nr = r;
            int nc = c;
            while (true) {
                nr += dr[d];
                nc += dc[d];
                if (nr >= n || nc >= n || nr < 0 || nc < 0) break;
                if (board[r][c] == board[nr][nc]) continue;
                int y = believe[nr][nc];
                if (x > y) {
                    board[nr][nc] = board[r][c];
                    believe[nr][nc] += 1;
                    x -= y + 1;
                } else {
                    board[nr][nc] = board[nr][nc] | board[r][c];
                    believe[nr][nc] += x;
                    x = 0;
                }
                protect[nr][nc] = true;

                if (x == 0) break;
            }


        }
    }

    private static void lunch() {
        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]) continue;
                visited[i][j] = true;
                Queue<int[]> q = new ArrayDeque<>();
                q.add(new int[]{i, j});
                int rr = i, rc = j;
                int cnt = 0;
                while (!q.isEmpty()) {
                    int[] poll = q.poll();
                    int r = poll[0], c = poll[1];
                    cnt += 1;
                    if (believe[r][c] > believe[rr][rc]
                            || (believe[r][c] == believe[rr][rc] && (r < rr || (r == rr && c < rc)))) {
                        rr = r;
                        rc = c;
                    }

                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];
                        if (nr >= n || nc >= n || nr < 0 || nc < 0 || board[nr][nc] != board[r][c] || visited[nr][nc])
                            continue;
                        visited[nr][nc] = true;
                        q.add(new int[]{nr, nc});
                    }
                }
                believe[rr][rc] += cnt;
                int weight = 1;
                if (board[rr][rc] == 7) weight = 2;
                Set<Integer> temp = new HashSet<>();
                temp.add(1);
                temp.add(2);
                temp.add(4);
                if (temp.contains(board[rr][rc])) weight = 0;
                pq.offer(new int[]{weight, rr, rc});
            }
        }
    }
}