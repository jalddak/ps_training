package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_2239 {
    private static int[][] board = new int[9][9];
    private static Set<Integer>[] rowCheck, colCheck, blockCheck;
    private static Stack<int[]> blanks = new Stack<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        rowCheck = new HashSet[9];
        colCheck = new HashSet[9];
        blockCheck = new HashSet[9];

        for (int i = 0; i < 9; i++) {
            String[] temp = br.readLine().split("");
            board[i] = Arrays.stream(temp).mapToInt(Integer::parseInt).toArray();
            rowCheck[i] = new HashSet<>();
            colCheck[i] = new HashSet<>();
            blockCheck[i] = new HashSet<>();
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int blockIndex = i / 3 * 3 + j / 3;
                rowCheck[i].add(board[i][j]);
                colCheck[i].add(board[j][i]);
                blockCheck[blockIndex].add(board[i][j]);
                if (board[i][j] == 0) blanks.push(new int[]{i, j});
            }
        }

        Collections.reverse(blanks);

        backTracking();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append(board[i][j]);
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }

    private static boolean backTracking() {
        boolean result = false;
        if (blanks.isEmpty()) return true;

        int[] yx = blanks.pop();
        int y = yx[0], x = yx[1];
        int blockIndex = y / 3 * 3 + x / 3;
        for (int num = 1; num < 10; num++) {
            if (rowCheck[y].contains(num) || colCheck[x].contains(num) || blockCheck[blockIndex].contains(num))
                continue;

            rowCheck[y].add(num);
            colCheck[x].add(num);
            blockCheck[blockIndex].add(num);

            board[y][x] = num;
            result = backTracking();

            rowCheck[y].remove(num);
            colCheck[x].remove(num);
            blockCheck[blockIndex].remove(num);

            if (result) break;
        }
        blanks.push(yx);

        return result;
    }
}
