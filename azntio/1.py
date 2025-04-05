from collections import deque
def bfs(start,graph):
    queue=deque()
    visited=set()
    to=[]
    queue.append(start)
    visited.add(start)
    while queue:
        cn=queue.popleft()
        to.append(cn)
        for nei in graph.get(cn,[]):
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
    return to

if __name__=="__main__":
    graph=[
        'A' ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    ]
    
    print("BFS Traversal:")
    result = bfs(graph, 'A')
    print(" -> ".join(result))
            
