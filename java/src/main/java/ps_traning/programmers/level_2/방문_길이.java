package ps_traning.programmers.level_2;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class 방문_길이 {
    class Location{
        int y;
        int x;
        public Location(int y, int x){
            this.y = y;
            this.x = x;
        }

        @Override
        public boolean equals(Object o){
            if(this == o) return true;
            if(o == null || getClass() != o.getClass()) return false;
            Location l = (Location) o;
            return y == l.y && x == l.x;
        }

        @Override
        public int hashCode(){
            return Objects.hash(y, x);
        }
    }


    public int solution(String dirs) {
        int answer = 0;
        int[] dy = new int[]{-1, 0, 1, 0};
        int[] dx = new int[]{0, 1, 0, -1};
        Map<Character, Integer> dirInfo = new HashMap<>();
        dirInfo.put('U', 0);
        dirInfo.put('R', 1);
        dirInfo.put('D', 2);
        dirInfo.put('L', 3);
        int y = 0;
        int x = 0;
        Map<Location, boolean[]> visited = new HashMap<>();

        for(char direction:dirs.toCharArray()){
            int d = dirInfo.get(direction);
            int ny = y + dy[d];
            int nx = x + dx[d];
            int rd = (d >= 2) ? d-2 : d+2;

            if(ny > 5 || ny < -5 || nx > 5 || nx < -5) continue;
            boolean[] b_visited = visited.getOrDefault(new Location(y, x), new boolean[4]);
            if(!b_visited[d]){
                b_visited[d] = true;
                visited.put(new Location(y, x), b_visited);

                boolean[] n_visited = visited.getOrDefault(new Location(ny, nx), new boolean[4]);
                n_visited[rd] = true;
                visited.put(new Location(ny, nx), n_visited);
                answer++;
            }
            y = ny;
            x = nx;
        }
        return answer;
}
