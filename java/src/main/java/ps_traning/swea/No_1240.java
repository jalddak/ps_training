package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class No_1240 {
    public static Map<Integer, Integer> scanner = new HashMap<>();

    public static void main(String[] args) throws IOException {
        scanner.put(211, 0);
        scanner.put(221, 1);
        scanner.put(122, 2);
        scanner.put(411, 3);
        scanner.put(132, 4);
        scanner.put(231, 5);
        scanner.put(114, 6);
        scanner.put(312, 7);
        scanner.put(213, 8);
        scanner.put(112, 9);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int m = Integer.valueOf(st.nextToken());

            int[][] board = new int[n][m];
            for (int i = 0; i < n; i++) {
                board[i] = br.readLine().chars().map(c -> c - '0').toArray();
            }

            int code = 0;
            int codeLen = 0;
            for (int i = 0; i < n; i++) {
                Set<Integer> set = Arrays.stream(board[i]).boxed().collect(Collectors.toSet());
                if (set.size() == 1) continue;

                int flag = 0;
                int num = board[i][0];
                int numCnt = 0;
                int checkNum = 0;
                for (int j = 0; j < m; j++) {

                    if (num == board[i][j]) {
                        numCnt++;
                        continue;
                    }
                    checkNum *= 10;
                    checkNum += numCnt;
                    flag += 1;
                    if (flag == 4) {
                        flag = 0;
                        checkNum %= 1000;
                        code *= 10;
                        codeLen += 1;
                        code += scanner.get(checkNum);
                        checkNum = 0;
                    }
                    if (codeLen == 8) break;
                    num = board[i][j];
                    numCnt = 1;
                }
                break;
            }

            int result = 0;
            int candidate = 0;
            int decoding = 0;
            for (int i = 0; i < 8; i++) {
                int temp = code % 10;
                code /= 10;
                candidate += temp;
                temp *= i % 2 == 1 ? 3 : 1;
                decoding += temp;
            }

            if (decoding % 10 == 0) {
                result = candidate;
            }

            sb.append(result).append("\n");
        }

        System.out.print(sb.toString());
    }
}
