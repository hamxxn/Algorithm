graph = [[], [2, 3, 7], [1, 4, 6], [1, 5, 7], [2, 6], [3, 7], [2, 4], [1, 3]]

visited = [False] * 9


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def dfs2(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque

    visited = []
    need_visited = deque()

    ##시작 노드 설정해주기
    need_visited.append(start_node)

    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()

        ##만약 방문한 리스트에 없다면
        if node not in visited:

            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])

    return visited


print(dfs2(graph, 1))
