package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class No_19236 {

    private static int[] dy = {0, -1, -1, 0, 1, 1, 1, 0, -1};
    private static int[] dx = {0, 0, -1, -1, -1, 0, 1, 1, 1};
    private static int result = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] board = new int[4][4];
        Map<Integer, Integer> directions = new HashMap<>();
        Map<Integer, int[]> locations = new HashMap<>();

        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                int num = Integer.parseInt(st.nextToken());
                int d = Integer.parseInt(st.nextToken());
                board[i][j] = num;
                directions.put(num, d);
                locations.put(num, new int[]{i, j});
            }
        }

        directions.put(0, directions.get(board[0][0]));
        directions.put(board[0][0], 0);
        locations.put(0, new int[]{0, 0});
        result += board[0][0];
        board[0][0] = 0;

        recursion(board, result, directions, locations);
        System.out.println(result);

    }

    private static void recursion(int[][] board, int temp
            , Map<Integer, Integer> directions, Map<Integer, int[]> locations) {

        result = Math.max(result, temp);
        fishMove(board, directions, locations);

        int d = directions.get(0);
        int[] loca = locations.get(0);
        int y = loca[0], x = loca[1];
        int ny = y, nx = x;
        while (true) {
            ny += dy[d];
            nx += dx[d];
            if (ny >= 4 || nx >= 4 || ny < 0 || nx < 0) break;
            if (board[ny][nx] > 16 || board[ny][nx] < 1) continue;
            int[][] cBoard = new int[4][4];
            Map<Integer, Integer> cDirections = new HashMap<>();
            Map<Integer, int[]> cLocations = new HashMap<>();
            copy(board, cBoard, directions, cDirections, locations, cLocations);

            int fish = cBoard[ny][nx];
            cDirections.put(0, cDirections.get(fish));
            cDirections.put(fish, 0);
            cLocations.put(0, cLocations.get(fish));
            cBoard[ny][nx] = 0;
            cBoard[y][x] = -1;

            recursion(cBoard, temp + fish, cDirections, cLocations);
        }


    }

    private static void copy(int[][] board, int[][] cBoard
            , Map<Integer, Integer> directions, Map<Integer, Integer> cDirections
            , Map<Integer, int[]> locations, Map<Integer, int[]> cLocations) {

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cBoard[i][j] = board[i][j];
                int idx = i * 4 + j + 1;
                cDirections.put(idx, directions.get(idx));
                cLocations.put(idx, new int[]{locations.get(idx)[0], locations.get(idx)[1]});
            }
        }

        cDirections.put(0, directions.get(0));
        cLocations.put(0, new int[]{locations.get(0)[0], locations.get(0)[1]});

    }

    private static void fishMove(int[][] board
            , Map<Integer, Integer> directions, Map<Integer, int[]> locations) {

        for (int i = 1; i <= 16; i++) {
            int d = directions.get(i);
            if (d == 0) continue;

            int[] loca = locations.get(i);
            int y = loca[0], x = loca[1];

            d -= 1;
            for (int t = 0; t < 7; t++) {
                d++;
                d = d > 8 ? d % 8 : d;
                int ay = y + dy[d];
                int ax = x + dx[d];
                if (ay >= 4 || ax >= 4 || ay < 0 || ax < 0 || board[ay][ax] == 0) continue;

                directions.put(i, d);
                locations.get(i)[0] = ay;
                locations.get(i)[1] = ax;
                board[y][x] = board[ay][ax];
                board[ay][ax] = i;
                if (board[y][x] == -1) break;

                locations.get(board[y][x])[0] = y;
                locations.get(board[y][x])[1] = x;
                break;

            }
        }
    }
}
