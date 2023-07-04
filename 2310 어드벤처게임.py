def CreateMaze(n): #입력받은 값 토대로 미로 생성
    room = [[]]

    for i in range(n) :
        r = ''
        while True:
            j = input()
            r = r + j
            if(r[-1] == '0'):
                list = r.split()
                graph.append(list[2:len(list)-1])

                room.append(list)
                break
            else :
                r += ' '

    return room
def dfs(graph, v, visited) :
    #v는 시작위치
    visited[v] = True


    #현재 노드와 연결된 노드를 재귀적으로 호출
    for i in graph[v]:
        if not visited[int(i)]:
            dfs(graph,int(i),visited)

def AdventureGame(graph, v, visited,m) :


    # 빈 방인 경우
    if(room[v][0] == 'E'):
        # v는 시작위치
        visited[v] = True


        # 현재 노드와 연결된 노드를 재귀적으로 호출
        for i in graph[v]:
            if not visited[int(i)]:
                AdventureGame(graph, int(i), visited,m)
    # 레플리콘인 경우
    elif(room[v][0] == 'L'):
        # v는 시작위치
        visited[v] = True


        cost = int(room[v][1])
        if(m < cost):
            m = cost


        # 현재 노드와 연결된 노드를 재귀적으로 호출
        for i in graph[v]:
            if not visited[int(i)]:
                AdventureGame(graph, int(i), visited,m)

    # 트롤인 경우
    elif(room[v][0] == 'T'):
        cost = int(room[v][1])
        if(m >= cost):
            # v는 시작위치
            visited[v] = True

            m -= cost
            for i in graph[v]:
                if not visited[int(i)]:
                    AdventureGame(graph, int(i), visited, m)
        else :
            return


while True :
    visited = [False] * 1000
    graph = [[]]
    n = int(input())
    m = 0 #소지금
    if(n == 0):
        break
    room = []
    room = CreateMaze(n)

    AdventureGame(graph,1,visited,m)

    if(visited[n] == True):
        print('Yes')
    else:
        print('No')

