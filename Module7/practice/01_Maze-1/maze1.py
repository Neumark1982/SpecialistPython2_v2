# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    ...
]

# Решите задачу и выведите ответ в нужном формате
def dfs(start_vertex, graph):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


graph = [
    [1],
    [0, 5],
    [6],
    [7],
    [5,8],
    [1,4],
    [2,10],
    [3],
    [4,9,12],
    [8,10],
    [9,6,11,14],
    [10],
    [8],
    [],
    [10,15],
    [14]
]

start = {'S-1':1, 'S-2':12, 'S-3':3}
finish = 14

for key, value in start.items():
    result = dfs(value, graph)
    if result[finish]:
        print(f"Из точки {key} можно дойти до финиша")
    else:
        print(f"Из точки {key} нельзя дойти до финиша")
