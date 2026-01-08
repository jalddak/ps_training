import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        boolean[][] board = new boolean[h][w];
        for (int i = 0; i < w; i++) {
            int input = Integer.parseInt(st.nextToken());
            for (int j = 0; j < input; j++) {
                board[j][i] = true;
            }
        }

        int answer = 0;
        for (int i = 0; i < h; i++) {
            boolean flag = false;
            int temp = 0;
            for (int j = 0; j < w; j++) {
                if (board[i][j]) {
                    if (flag) answer += temp;
                    temp = 0;
                    flag = true;
                } else temp += 1;
            }
        }

        System.out.println(answer);
    }
}