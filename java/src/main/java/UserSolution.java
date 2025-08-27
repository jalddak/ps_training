import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class UserSolution {

    Map<Integer, int[]> solInfo;
    Map<Integer, Map<Integer, Set<Integer>>> teamInfo;

    public void init() {
        solInfo = new HashMap<>();
        teamInfo = new HashMap<>();
    }

    public void hire(int mID, int mTeam, int mScore) {
        solInfo.put(mID, new int[]{mTeam, mScore});
        if (!teamInfo.containsKey(mTeam)) teamInfo.put(mTeam, new HashMap<>());
        if (!teamInfo.get(mTeam).containsKey(mScore)) teamInfo.get(mTeam).put(mScore, new HashSet<>());
        teamInfo.get(mTeam).get(mScore).add(mID);

    }

    public void fire(int mID) {
        teamInfo.get(solInfo.get(mID)[0]).get(solInfo.get(mID)[1]).remove(mID);
        solInfo.remove(mID);
    }

    public void updateSoldier(int mID, int mScore) {
        solInfo.get(mID)[1] = mScore;
    }

    public void updateTeam(int mTeam, int mChangeScore) {

    }

    public int bestSoldier(int mTeam) {
        return 0;
    }
}