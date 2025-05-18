# 정확성은 게속 맞았는데, 효율성에서 게속 틀렸다.

def solution(alp, cop, problems):
    max_alp = alp
    max_cop = cop
    for p in problems:
        max_alp = max(max_alp,p[0])
        max_cop = max(max_cop,p[1])
    # 1-1 도움받은 부분 (시간을 줄여주는데 도움됨) 1-2와 연결
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp = [[300 for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    # 1-2 도움받은 부분 (alp, cop 부터 탐색해서 시간을 줄여줌)
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):

            # -------------------------------- #
            # 따라서 이 사이에 있는 코드는 dp[alp][cop] = 0 이상의 효과를 내진 않음
            if i <= alp and j <= cop:
                dp[i][j] = 0
            # -------------------------------- #
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = p
                if i >= alp_req and j >= cop_req:
                    # 2-1 도움받은 부분
                    # 넘어가는 부분에서 최소값이 나올 수 있으므로 경계를 정해서 max_alp, max_cop 에서 최소값을 가지도록
                    # next_alp, next_cop 를 만들어줬다.
                    next_alp, next_cop = min(max_alp,i + alp_rwd), min(max_cop,j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j]+cost)
    
    answer = dp[-1][-1]
    return answer