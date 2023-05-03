from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    dist = {source: (0, 0)} 
    visited = set()
    pq = [(0, 0, source)] 
    
    while pq:
        (weight, edges, node) = heappop(pq)
        
        if node not in visited:
            visited.add(node)
            for neighbor, edge_weight in graph[node]:
                new_weight = weight + edge_weight
                new_edges = edges + 1
                if neighbor not in dist or (new_weight, new_edges) < dist[neighbor]:
                    dist[neighbor] = (new_weight, new_edges)
                    heappush(pq, (new_weight, new_edges, neighbor))
                elif neighbor not in visited and neighbor not in dist:
                    dist[neighbor] = (float('inf'), float('inf'))
    
    return dist
    
    
    pass
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = {source: None}
    visited = set([source])
    queue = deque([source])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = node
                queue.append(neighbor)

    return parents
    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    current = destination
    while current in parents:
        path.append(current)
        current = parents[current]
    path.reverse()
    return ''.join(path[:-1])
    pass

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'
