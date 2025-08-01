package ps_traning.algostudy._250804;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_12869 {

    private static int n, result;

    /**
     * visited 3차원 배열로 크기 제한은 61로 다 준 이유: scv 3마리 밖에 생성 못하고 최대 hp가 60 이라서. - 체력수치 기준으로 visited 체크
     * ps: 한 사이클에 할 수 있는 공격력 수치
     * idxs: 지금 생각해보니까 굳이 없어도 될 것 같음. ps랑 병합해서 ps에서 한번에 나타내는게 더 좋아보임.
     */
    private static boolean[][][] visited = new boolean[61][61][61];
    private static int[] ps = {1, 3, 9};
    private static int[][] idxs = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[] scvs = new int[3];


        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            scvs[i] = Integer.parseInt(st.nextToken());
            // result의 최대값을 그냥 모든 scvs의 체력의 합으로 하면 무조건 낮아질 수 밖에 없음. 안전한 인트범위임.
            result += scvs[i];
        }

        // 정렬을 하면서 같은 체력의 경우 ( 1, 3, 5 ) / (3, 1, 5) 같은 경우도 그냥 이미 체크했던 체력들이라고 표시 가능함.
        Arrays.sort(scvs);
        Queue<int[]> q = new ArrayDeque<>();
        visited[scvs[0]][scvs[1]][scvs[2]] = true;
        // q의 원소는 {체력1, 체력2, 체력3, 공격횟수} 라고 생각할 수 있음.
        q.offer(new int[]{scvs[0], scvs[1], scvs[2], 0});

        while (!q.isEmpty()) {
            int[] poll = q.poll();
            if (poll[0] == 0 && poll[1] == 0 && poll[2] == 0) {
                result = poll[3];
                break;
            }
            for (int i = 0; i < idxs.length; i++) {
                for (int j = 0; j < 3; j++) {
                    scvs[j] = Math.max(poll[j] - ps[idxs[i][j]], 0);
                }
                Arrays.sort(scvs);
                if (visited[scvs[0]][scvs[1]][scvs[2]]) continue;
                visited[scvs[0]][scvs[1]][scvs[2]] = true;
                q.offer(new int[]{scvs[0], scvs[1], scvs[2], poll[3] + 1});
            }
        }
        System.out.println(result);
    }
}