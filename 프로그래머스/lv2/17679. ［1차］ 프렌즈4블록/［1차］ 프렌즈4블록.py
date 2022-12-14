def solution(m, n, board):
    # input: m은 행의 개수, n의 열의 개수
    # output: 몇 개 블록이 지워질지
    answer = 0 # 총 사라진 블록 수 
    
    # board를 2차원 list로
    b = [[j for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = board[i][j] 
            # tip: for i in range(m): board[i] = list(board[i])
                  # b = [list(x) for x in board]
                
    # issue: 어떻게 없어진 애 처리?
    # 2*2 찾고 0으로 -> 0인 애들은 무시하고 2*2를 찾게
    while True: # 알아서 종료될 때까지 돌림
    # issue: 어떻게 2*2 블록이 겹쳐있을 때 처리? -> set(집합) 사용
        pop = [] # 이번에 터져야 할 블록들 모음
        for i in range(m-1):
            for j in range(n-1):
                if b[i][j] == b[i][j+1] == b[i+1][j] == b[i+1][j+1] != '0': # tip
                    pop.append((i,j))
                    pop.append((i+1,j))
                    pop.append((i,j+1))
                    pop.append((i+1,j+1))
        if len(pop) == 0:
            break
        answer += len(set(pop)) # 터져야 할 블록 처리하기
        for p in pop:
            b[p[0]][p[1]] = '0'
        
        # issue: 블록들 내리기-> 블록이 아래로 떨어져 빈 공간을 채우는 부분 
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if b[i+1][j] == '0': #아래가 비어있다면
                        b[i+1][j] = b[i][j]  
                        b[i][j] = '0'
    return answer
