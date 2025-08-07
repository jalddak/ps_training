package ps_traning.algostudy._250812.programmers;

class No_1843 {
    public int solution(String arr[]) {
        int answer = -1;

        int len = arr.length;
        int n = len / 2 + 1;

        int[] nums = new int[n];
        String[] ops = new String[n - 1];
        for (int i = 0; i < len; i++) {
            if (i % 2 == 0) nums[i / 2] = Integer.parseInt(arr[i]);
            else ops[i / 2] = arr[i];
        }

        int[][] maxDp = new int[n][n];
        int[][] minDp = new int[n][n];
        int minNum = -1000 * 101;
        int maxNum = 1000 * 101;
        for (int i = 0; i < n; i++) {
            maxDp[i][i] = nums[i];
            minDp[i][i] = nums[i];
            for (int j = i + 1; j < n; j++) {
                maxDp[i][j] = minNum;
                minDp[i][j] = maxNum;
            }
        }

        for (int r = 1; r < n; r++) {
            for (int i = 0; i < n - r; i++) {
                for (int j = i; j < i + r; j++) {
                    int maxTemp = ops[j].equals("+") ? maxDp[j + 1][i + r] : -minDp[j + 1][i + r];
                    int minTemp = ops[j].equals("-") ? -maxDp[j + 1][i + r] : minDp[j + 1][i + r];
                    maxDp[i][i + r] = Math.max(maxDp[i][i + r], maxDp[i][j] + maxTemp);
                    minDp[i][i + r] = Math.min(minDp[i][i + r], minDp[i][j] + minTemp);
                }
            }
        }

        answer = maxDp[0][n - 1];
        return answer;
    }
}