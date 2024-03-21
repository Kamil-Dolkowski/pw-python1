mapa = {
    'A':{'B':2,'D':4},
    'B':{'C':3,'D':3},
    'C':{'E':2},
    'D':{'C':3,'E':4},
    'E':{}
}


def algorytm_dijkstry(graph, start, goal):
    # Ustaw odległości na nieskończoność
    shortest_distances = { vortex:float('infinity') for vortex in graph }
    # Dla wierzchołka startowego ustaw wartość 0
    shortest_distances[start] = 0
    predecessors = {}
    # Nieodwiedzone wierzchołki
    unvisited = graph.copy()
    # Pętle nieodwiedzonych wierzchołków
    while unvisited:
        # Wybierz wierzchołek z najmniejszą odległością
        current_min_vortex = None
        for vortex in unvisited:
            if current_min_vortex is None:
                current_min_vortex = vortex
            elif shortest_distances[vortex] < shortest_distances[current_min_vortex]:
                current_min_vortex = vortex

        # Sprawdź wszystkich sąsiadów aktualnego wierzchołka
        for neighbour, cost in graph[current_min_vortex].items():
            if cost + shortest_distances[current_min_vortex] < shortest_distances[neighbour]:
                shortest_distances[neighbour] = cost + shortest_distances[current_min_vortex]
                predecessors[neighbour] = current_min_vortex
        # Usuń z listy przetworzony wierzchołek
        unvisited.pop(current_min_vortex)
    # Odtworzenie ścieżki od startu do celu
    current_vortex = goal
    path = []

    while current_vortex != start:
        path.append(current_vortex)
        current_vortex = predecessors[current_vortex]
    path.append(start)

    return path[::-1], shortest_distances[goal]


path, distance = algorytm_dijkstry(mapa, 'A', 'E')

print(f"Najkrótsza ścieżka: {path}, długość: {distance}")









# --------------------------Algorytm Dijkstry--------------------------

    # Ustaw odległości na nieskończoność

        # Dla wierzchołka startowego ustaw wartość 0

        # Nieodwiedzone wierzchołki

        # Pętle nieodwiedzonych wierzchołków

            # Wybierz wierzchołek z najmniejszą odległością
        
            # Sprawdź wszystkich sąsiadów aktualnego wierzchołka
        
            # Usuń z listy przetworzony wierzchołek
        
        # Odtworzenie ścieżki od startu do celu
