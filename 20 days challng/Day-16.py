#Iterative DFS
def dfs_iterative(graph, start):
    visited = set()  
    stack = [start]  

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  
            visited.add(node)
            
            stack.extend(reversed(graph[node]))

print("\nDFS (Iterative):", end=" ")
dfs_iterative(graph, 0)  


#Recursive DFS
def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")  
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

visited = set()  
print("DFS (Recursive):", end=" ")
dfs_recursive(graph, 0, visited)  
